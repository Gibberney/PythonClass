import folium
import pandas

data = pandas.read_csv("volcanoes_usa.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
        if elevation < 1000:
            return 'green'
        elif 1000<=elevation< 3000:
            return 'orange'
        else: 
            return 'red'

map = folium.Map(location = [38.58, -99.09], zoom_start=4, tiles="Mapbox Bright")


fg=folium.FeatureGroup(name="my map")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=7, color='grey', fill=True, fill_color=color_producer(el), 
    fill_opacity=1, popup=str(el)+" m", icon=folium.Icon(color=color_producer(el))))





map.add_child(fg)

map.save("Map1.html")
