from imba import create_html
from map_lib import map_area
from create import generat as g
from dannie import *
from loc import cord_gen
import geopy.distance
import random, ast
import pandas as pd

#экселька с данными
file_name = 'data/vse.xlsx'
x = dan(file_name)
x.read()

# стартовые корды
start_x=37
start_y=56

# генератор квадратов
squares = g.squares(50, 50,start_x,start_y)
area_dan = []
for i in squares:
   rand_density = random.randint(1, 10000)
   area_dan.append(["25","",rand_density,[[i]]])
posts = []

post_in_area = []
#тестовые точки
# posts.append(["шесть", 234, 1104, [37.019, 56.010]])
# posts.append(["сэмь", 234, 1104, [37.023, 56.003]])
# for area in range(len(squares)):
#         if squares[area][0][0]>=37.019>=squares[area][3][0] and squares[area][0][1]>=56.010>=squares[area][1][1]:
#             post_in_area.append([[37.019, 56.010],area])
#         else:
#             print("False")
# for area in range(len(squares)):
#         if squares[area][0][0]>=37.023>=squares[area][3][0] and squares[area][0][1]>=56.003>=squares[area][1][1]:
#             post_in_area.append([[37.023, 56.003],area])
#         else:
            # print("False")
            # ...

# генератор домов
for i in range(31468):
   cord = ast.literal_eval(x.cord[i])
   cord.reverse()
   posts.append([str(x.adres[i]),int(x.peoples[i]),int(x.apartments[i]), cord])
   for area in range(len(squares)):
        if squares[area][0][0]>=cord[0]>=squares[area][3][0] and squares[area][0][1]>=cord[1]>=squares[area][1][1]:
            zv = area
            yv=0
            while zv >=50:
               zv=zv-50
               yv+=1
            xv=zv
            post_in_area.append([cord,(yv,xv)])

#кол-во квадратов заполненых постматами
cvadrat = 50
#генератор постоматов
p = g.postomsts(5,start_x,start_y,cvadrat)



#генератор json
map_area.gen_json_area(area_dan)

map_area.gen_json_point(posts)
# генератор маршрутов





rote_list = []


out_dan_1 = []
out_dan_2 = []
out_dan_3 = []
end = len(post_in_area)
for i in post_in_area:
   end-=1
   print(end)
   for j in range(len(p)):
      if (i[1][0]+i[1][1]*50)*25<=j<((i[1][0]+i[1][1]*50)*25)+25:
         rote_list.append([p[j],i[0]])
         # dist = geopy.distance.geodesic([p[j],i[0]])
         # distance = dist.m
         # distance = float('{:.1f}'.format(distance))
         out_dan_1.append(i[1])
         out_dan_2.append(j-((i[1][0]+i[1][1]*50)*25))
         out_dan_3.append(float('{:.1f}'.format(geopy.distance.geodesic(p[j],i[0]).m)))
# Append data in .csv table
df = pd.DataFrame({"Область":out_dan_1,"Элемент":out_dan_2,"Дистанция":out_dan_3})
df.to_excel("output.xlsx", header=False, index=False)




map_area.gen_json_routes(rote_list)


#генератор html
create_html(len(posts))