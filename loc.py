import geopy
from geopy.geocoders import Nominatim


def cord_gen(addr):
    try:
        x=[]
        if "к. " in addr:

            x.append(""+addr.replace("к. ",
                        "корпус ").rstrip(',').replace("ё", "е"))
        if " Москва" in addr:

            x.append(""+addr.replace(" Москва",
                        "").rstrip(',').replace("ё", "е"))

            addr = x
        USERAGENT = 'https://www.wikipedia.org'
        # addr = 'ул. Расплетина, д. 21, Москва' # адрес
        geolocator = Nominatim(timeout=10, user_agent=f"{USERAGENT}")

        location = geolocator.geocode(addr, language="ru")
        # точный адрес
        # print(location)
        # координаты
        cords = [round((location.longitude), 5), round((location.latitude), 5)]
        # print(location.latitude, location.longitude)
        

        return cords
    except:
        # print(f'{addr} - не найден')
        ...
