import geopy.distance

dist = geopy.distance.geodesic([37.46097, 55.7754],[37.47393, 55.75401]
)
distance = dist.m
distance = float('{:.1f}'.format(distance))


print(f"{distance} меторв")