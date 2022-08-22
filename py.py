import folium
map = folium.Map(location=[55.65310221424613, 12.142294332895851], zoom_start=16)
#do -> dir(folium) ... to get a list of folium directory
#do -> help(folium.map) ... to see what you can pass to it
# folium makes a map by converting python into js & html/css.
map.save("Map1.html")
# ^ This creates the html file