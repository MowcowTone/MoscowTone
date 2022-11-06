### `local.py` - утилита, которая конвнртирует **адрес** в **координаты**

```python

from geopy.geocoders import Nominatim
from dotenv import load_dotenv, find_dotenv
from dannie import dan
import geopy, geocoder, pandas, os


# USERAGENT - сервер, с которого производится поиск
USERAGENT = 'https://yourdomain.com'

d = dan("./data/chelovek_4.xlsx") # таблица с адресами для чтения
d.read()
home = [] # массив адресов
ap = [] # массив квартир
cord = [] # массив координат
count = 2500 # счетчик
for i in range(2500):
    try:
        home.append(d.adres[i])
        ap.append(d.Apartments[i])
        geolocator = geocoder.tomtom(d.adres[i], key='<API_KEY>')
        # Счетчик
        count -= 1
        # вывод прогресса
        print(f"{count}) {geolocator.latlng}")
        # добавление координат в список (таблица Excel)
        cord.append(geolocator.latlng)
    except:
        pass
# добавление данных в таблицу
df = pandas.DataFrame({"адрес":home,"координаты":cord,"квартир":ap})
# Создание таблицы с результатом
df.to_excel('data/vse.xlsx')
```