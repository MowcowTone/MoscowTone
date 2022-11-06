### How to use MAP API

```python
import folium

# Создание карты
# location=[40.75834,30.38001] - начальная точка координат
# zoom_start = 8 - начальный зум карты
m = folium.Map(location=[40.75834,30.38001], zoom_start=8)

folium.Marker(location=[40.75834,30.38001], popup =  'Sakarya').add_to(m)

folium.Circle(location=(40.75834,30.38001),radius=500, fill_color='blue').add_to(m)
folium.Circle(location=(40.45834,30.28001),radius=500, fill_color='blue').add_to(m)

# ниже сохраняю карту

m.save("markers.html")
```