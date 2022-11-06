import folium, geopandas, branca, base64, os
import osmnx as ox
import networkx as nx
from folium.plugins import Search
from folium import IFrame

def create_html(len_points):
    states = geopandas.read_file(
        # File with square areas
        "data/area.json",
        driver="GeoJSON",
    )

    cities = geopandas.read_file(
        # File with Points
        "data/points.json",
        driver="GeoJSON",
    )

    states_sorted = states.sort_values(by="density", ascending=False)

    states_sorted.head(5).append(states_sorted.tail(5))[["name", "density"]]

    def rd2(x):
        return round(x, 2)


    minimum, maximum = states["density"].quantile([0.05, 0.95]).apply(rd2)

    mean = round(states["density"].mean(), 2)


    print(f"minimum: {minimum}", f"maximum: {maximum}", f"Mean: {mean}", sep="\n\n")



    colormap = branca.colormap.LinearColormap(
        colors=["#f2f0f7", "#DEFFDE", "#B8FFB8", "#68FF68", "#00FF00"],
        # colors=["#f2f0f7", "#cbc9e2", "#9e9ac8", "#756bb1", "#54278f"],
        index=states["density"].quantile([0.2, 0.4, 0.6, 0.8]),
        vmin=minimum,
        vmax=maximum,
    )

    colormap.caption = "Плотность населения"

    cities = geopandas.sjoin(cities, states, how="inner", predicate="within")
    pop_ranked_cities = cities.sort_values(by="pop_max", ascending=False)[
        ["nameascii", "pop_max", "geometry"]
    ].iloc[:len_points]
    print(pop_ranked_cities)
    # pop_ranked_cities.head(5)

    m = folium.Map(location=[56, 37], zoom_start=8)


    """ ROUTES """


    # graph_start = [37.01, 56.005]
    # graph_end = [37.015, 56.004]

    # route_marker = './images/marker.png'
    # icons_size = (20,20)
    # html = '<img src="data:image/png;base64,{}">'.format

    routesData = os.path.join('data/routes.json')

    folium.GeoJson(routesData, name='Маршрут').add_to(m)

    # icon1 = folium.features.CustomIcon(f'{route_marker}', icon_size=icons_size)
    # marker1 = folium.Marker(location=graph_start, icon=icon1).add_to(m)

    # icon2 = folium.features.CustomIcon(f'{route_marker}', icon_size=icons_size)
    # marker2 = folium.Marker(location=graph_end, icon=icon2).add_to(m)

    def style_function(x):
        return {
            "fillColor": colormap(x["properties"]["density"]),
            "color": "black",
            "weight": 2,
            "fillOpacity": 0.5,
        }

    stategeo = folium.GeoJson(
        states,
        name="Районы",
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(
            fields=["name", "density"], aliases=["", "Плотность населения"], localize=True
        ),
    ).add_to(m)

    citygeo = folium.GeoJson(
        pop_ranked_cities,
        name="Метки",
        tooltip=folium.GeoJsonTooltip(
            fields=["nameascii", "pop_max"], aliases=["Дом", "Популяция"], localize=True
        ),
    ).add_to(m)

    statesearch = Search(
        layer=stategeo,
        geom_type="Polygon",
        placeholder="Найти район на карте",
        collapsed=False,
        search_label="name",
        weight=3,
    ).add_to(m)

    citysearch = Search(
        layer=citygeo,
        geom_type="Point",
        placeholder="Найти точку на карте",
        collapsed=True,
        search_label="nameascii",
    ).add_to(m)

    folium.LayerControl().add_to(m)
    colormap.add_to(m)

    m.save("imba.html")