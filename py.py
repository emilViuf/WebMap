import folium
map = folium.Map(location=[55.65310221424613, 12.142294332895851], zoom_start=10, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Locations")
fg.add_children(folium.Marker(location=[55.65310221424613, 12.142294332895851], popup="This is RUC", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[55.68376107342263, 12.514369497178908], popup="This is CBS", icon=folium.Icon(color='blue')))
map.add_child(fg)




mapwToner = folium.Map(location=[55.65310221424613, 12.142294332895851], zoom_start=10, tiles="Stamen toner")
mapwToner.add_child(folium.Marker(location=[55.65310221424613, 12.142294332895851], popup="This is RUC", icon=folium.Icon(color='green')))
mapwToner.add_child(folium.Marker(location=[55.68376107342263, 12.514369497178908], popup="This is CBS", icon=folium.Icon(color='blue')))

mapwColor = folium.Map(location=[55.65310221424613, 12.142294332895851], zoom_start=10, tiles="Stamen Water Color")
mapwColor.add_child(folium.Marker(location=[55.65310221424613, 12.142294332895851], popup="This is RUC", icon=folium.Icon(color='green')))
mapwColor.add_child(folium.Marker(location=[55.68376107342263, 12.514369497178908], popup="This is CBS", icon=folium.Icon(color='blue')))

#do -> help(folium.map) ... to see what you can pass to it
# folium makes a map by converting python into js & html/css.
map.save("Map1.html")
mapwToner.save("Map2.html")
mapwColor.save("Map3.html")

# ^ This creates the html file
