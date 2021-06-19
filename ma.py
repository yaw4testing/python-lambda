import folium
import pandas
# pandas.read_csv converts the volcanoes.txt into a data frame
data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"]) #we convert latitude and longitude column into a list[] for looping
lon = list(data["LON"])
elve = list(data['ELEV'])
name = list(data['NAME'])
fg = folium.FeatureGroup(name="My Map")

#adding a function call make the color of the icon dynamic
def color_picker(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'orange'
    else:
        return 'red'

html="""Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
 Height:%s m """
for lt,ln in zip(lat,lon):
    map1=folium.Map(location=[lt,ln], zoom_start=6, tiles="Stamen Terrain")
for lt,lng,ele,name in zip(lat,lon,elve,name): # using the zip() to group the lat[] and lon[] values into columns.
    #without the zip() function for loop can't handles the values in the two list[lat,lng]
    iframe = folium.IFrame(html=html % (name,name,ele),width=200, height=100)
   # fg.add_child(folium.Marker(location=[lt, lng], popup=folium.Popup(iframe), icon=folium.Icon(color=color_picker(ele))))
    fg.add_child(folium.CircleMarker(location=[lt,lng],popup=folium.Popup(iframe),radius=6,fill_color=color_picker(ele),color='grey'))
map1.add_child(fg)
map1.save("myMap.html")
