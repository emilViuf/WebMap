import folium
import pandas
map = folium.Map(location=[55.65310221424613, 12.142294332895851], zoom_start=10, tiles="Stamen Terrain")
mapwToner = folium.Map(location=[55.65310221424613, 12.142294332895851], zoom_start=10, tiles="Stamen toner")
mapwColor = folium.Map(location=[55.65310221424613, 12.142294332895851], zoom_start=10, tiles="Stamen Water Color")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[55.65310221424613, 12.142294332895851], popup="This is RUC", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[55.68376107342263, 12.514369497178908], popup="This is CBS", icon=folium.Icon(color='blue')))

fgT = folium.FeatureGroup(name="My Map")
fgT.add_child(folium.Marker(location=[55.65310221424613, 12.142294332895851], popup="This is RUC", icon=folium.Icon(color='green')))
fgT.add_child(folium.Marker(location=[55.68376107342263, 12.514369497178908], popup="This is CBS", icon=folium.Icon(color='blue')))

fgC = folium.FeatureGroup(name="My Map")
fgC.add_child(folium.Marker(location=[55.65310221424613, 12.142294332895851], popup="This is RUC", icon=folium.Icon(color='green')))
fgC.add_child(folium.Marker(location=[55.68376107342263, 12.514369497178908], popup="This is CBS", icon=folium.Icon(color='blue')))


map.add_child(fg)
mapwToner.add_child(fgT)
mapwColor.add_child(fgC)


#do -> help(folium.map) ... to see what you can pass to it
# folium makes a map by converting python into js & html/css.
map.save("Map1.html")
mapwToner.save("Map2.html")
mapwColor.save("Map3.html")
# ^ This creates the html file


#doing it with for loop instead
mapFor = folium.Map(location=[55.65310221424613, 12.142294332895851], zoom_start=10, tiles="Stamen Terrain")

fgfor = folium.FeatureGroup(name="My Map")

for coordinates in [[55.65310221424613, 12.142294332895851],[55.68376107342263, 12.514369497178908]]:
    fg.add_child(folium.Marker(location=coordinates, popup="This is a University", icon=folium.Icon(color='green')))

mapFor.add_child(fgfor)

map.save("MapFor.html")


#Creating Volcano map
VOLmap = folium.Map(location=[41.85022545174429, -118.2853730951305], zoom_start=7, tiles="Stamen Terrain")

#reading from txt file
dataVOL = pandas.read_csv("Volcanoes.txt")

#for coordinates in dataVOL
lon = list(dataVOL["LON"])
lat = list(dataVOL["LAT"])
name = list(dataVOL["NAME"])
elev = list(dataVOL["ELEV"])

#maybe go back and add html to popups?

#FeatureGroup / Child
fgVOL = folium.FeatureGroup(name="Volcano Map")
for lt, ln, nm, el in zip(lat, lon, name, elev):
    fgVOL.add_child(folium.Marker(location=[lt, ln], popup=["Name:" + str(nm) + "\n" + "Elevation:" + str(el) + " m"], icon=folium.Icon(color='blue')))
VOLmap.add_child(fgVOL)

#Create map
VOLmap.save("VOLmap.html")