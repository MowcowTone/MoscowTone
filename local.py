from geopy.geocoders import Nominatim
from dotenv import load_dotenv, find_dotenv
from dannie import dan
import geopy, geocoder, pandas, os

# Find `.env` file
load_dotenv(find_dotenv())

USERAGENT = 'https://www.wikipedia.org'

d = dan("./data/input/r_13_dan.xlsx")
d.read()
home = []
ap = []
cord = []
count = 2500
for i in range(2500):
    try:
        home.append(d.adres[i])
        ap.append(d.Apartments[i])
        geolocator = geocoder.tomtom(d.adres[i], key='your_key')
        count -= 1
        print(f"{count}) {geolocator.latlng}")
        cord.append(geolocator.latlng)
    except:
        pass
df = pandas.DataFrame({"адрес":home,"координаты":cord,"квартир":ap})
df.to_excel('./data/tables/r_13.xlsx')