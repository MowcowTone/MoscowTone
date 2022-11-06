
### Импортируемые библиотеки

```python
import pandas
import folium
from create import generat as g
```

### Считываются все пути, по которым, ищется ближайший постамат в области и записываются его координаты

```python
kv = pandas.read_excel("output.xlsx")["квадрат"]
tk = pandas.read_excel("output.xlsx")["точка"]
dl = pandas.read_excel("output.xlsx")["длинна"]
kvadrati = []
max_rost = 600
vhods = []
for i in kv:
    if i not in kvadrati:
        kvadrati.append(i)
print("этап 1")
ln_kv = len(kvadrati)
print(ln_kv)
for i in kvadrati:
    lists = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for k in range(len(kv)):
        if kv[k] == i:
            x_print = 0
            lists[tk[k]].append(dl[k])
    minim = 600
    for l in range(len(lists)):
        x=0
        for m in lists[l]:
            x+=m
        if (x/len(lists[l]))<= minim:
            minim = x/len(lists[l])
            end_el = l
    print(ln_kv)
    ln_kv-=1
    ls = i.strip('()').replace('"', '').replace(' ', '').split(',')
    vhods.append([ls,end_el,minim])
print("этап 2")

```

### Вывод всех постаматов

```python
# Создаю карту
m = folium.Map(location=[56.0025, 37.005])

start_x=37
start_y=56
cvadrat = 50
p = g.postomsts(5,start_x,start_y,cvadrat)


#vhods = [[(22,13),1,337],[(22,18),0,337]]
for vhod in vhods:
    cord = ((int(vhod[0][0])+int(vhod[0][1])*50)*25)+vhod[1]
    print(cord)

    print(len(p))
    revcords = p[cord]
    revcords.reverse()
    print(revcords)

    # Markers
    folium.Marker(location=revcords, popup=f"средняя&nbsp;длина: {vhod[2]}").add_to(m)

    # Circles
    folium.Circle(location=revcords,radius=500, fill_color='blue').add_to(m)

# сохраняю карту
print("всё")
m.save("markers.html")
```