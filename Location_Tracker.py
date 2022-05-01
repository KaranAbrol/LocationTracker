import phonenumbers

import folium
number = input("Enter the number:")


key = "2a5d8072fe6c45919290ffef1afc7a8a"

from phonenumbers import  geocoder
ch_number = phonenumbers.parse(number,"CH")
yourlocation = geocoder.description_for_number(ch_number,"en")
print(yourlocation)

from phonenumbers import carrier
service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(yourlocation)
print(query)
result = geocoder.geocode(query)

print(result)

lat = result[0]['geometry']['lat']

log = result[0]['geometry']['lng']

print(lat,log)

mymap = folium.Map(location = [lat,log],zoom_start = 9)

folium.Marker([lat,log], popup = yourlocation).add_to(mymap)



mymap.save("/Users/karanabrol/Desktop/project 2/myloc.html")
