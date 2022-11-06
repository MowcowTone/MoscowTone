from types import SimpleNamespace
import json
class map_area():
    def gen_json_area(lists):
        for i in range(len(lists)):
            id = lists[i][0]
            name = lists[i][1]
            density = lists[i][2]
            coordinates = lists[i][3]
            if i == 0:
                # JSon object
                # lists
                jsondata = {}
                features = [{}]
                properties = {}
                geometry = {}
                # props to lists
                features[0]["type"] = 'Feature' 
                features[0]["id"] = id

                properties['name'] = name
                properties['density'] = density
                # properties['pop_min'] = pop_min
                features[0]['properties'] = properties


                geometry["type"] = 'MultiPolygon'
                geometry["coordinates"] = coordinates 
                features[0]["geometry"] = geometry

                jsondata["type"] = 'FeatureCollection'
                jsondata["features"] = features
            else:
                features = [{}]
                properties = {}
                geometry={}
                features[0]["type"] = 'Feature' 
                features[0]["id"] = id
                properties['name'] = name
                properties['density'] = density
                # properties['pop_min'] = pop_min
                features[0]['properties'] = properties
                geometry["type"] = 'MultiPolygon'
                geometry["coordinates"] = coordinates 
                features[0]["geometry"] = geometry
                jsondata["features"] += features
        dump = json.dumps(jsondata)



        with open('data/area.json', 'w', encoding="utf-8") as f:
            f.write(dump)
            
    def gen_json_point(lists):
        for i in range(len(lists)):
            nameascii=lists[i][0]
            pop_min=lists[i][1]
            pop_max=lists[i][2]
            coordinates=lists[i][3]
            if i == 0:
                jsondata = {}
                features = [{}]
                properties = {}
                geometry={}

                jsondata["type"]="FeatureCollection"
                geometry["type"]="Point"
                geometry["coordinates"]=coordinates
                # jsondata["geometry"]=geometry
            
                features[0]["type"] = "Feature"
                features[0]['properties'] = properties 
                features[0]['geometry'] = geometry 

                properties["nameascii"] = nameascii
                properties["pop_max"] = pop_max
                properties["pop_min"] = pop_min
                jsondata["features"]=features

            else:
                features = [{}]
                properties = {}
                geometry={}
                geometry["type"]="Point"
                geometry["coordinates"]=coordinates
                features[0]["type"] = "Feature"
                features[0]['properties'] = properties 
                features[0]['geometry'] = geometry
                properties["nameascii"] = nameascii
                properties["pop_max"] = pop_max
                properties["pop_min"] = pop_min
                jsondata["features"]+=features
                
        dump = json.dumps(jsondata)

        with open('data/points.json', 'w', encoding="utf-8") as f:
            f.write(dump)
        
    def gen_json_routes(lists):
        for i in range(len(lists)):
            coordinates=lists[i]
            if i == 0:
                jsondata = {}
                features = [{}]
                properties = {}
                geometry={}

                jsondata["type"]="FeatureCollection"
                geometry["type"]="LineString"
                geometry["coordinates"]=coordinates
                # jsondata["geometry"]=geometry
            
                features[0]["type"] = "Feature"
                features[0]['properties'] = properties 
                features[0]['geometry'] = geometry 

                jsondata["features"]=features

            else:
                features = [{}]
                properties = {}
                geometry={}
                geometry["type"]="LineString"
                geometry["coordinates"]=coordinates
                features[0]["type"] = "Feature"
                features[0]['properties'] = properties 
                features[0]['geometry'] = geometry
                jsondata["features"]+=features
        dump = json.dumps(jsondata)
        with open('data/routes.json', 'w', encoding="utf-8") as f:
            f.write(dump)