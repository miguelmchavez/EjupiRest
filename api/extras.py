from math import radians, cos, sin, asin, sqrt
from api.models import Parada, Detalleparada
import math

def coordenadas(lat1, lon1, lat2, lon2):
    Paradas = Parada.objects.all()
    parada_origen = None 
    parada_destino = None
    au_distancia_origen = 0.0
    au_distancia_destino = 0.0
    distancia_origen = 0.0
    distancia_destino = 0.0
    for item in Paradas:
        if parada_origen == None:
            parada_origen = item
            parada_destino = item
            au_distancia_origen = distance(item.lat_parada, item.lng_parada, lat1, lon1)
            au_distancia_destino = distance(item.lat_parada, item.lng_parada, lat2, lon2)
        else:
            distancia_origen = distance(item.lat_parada, item.lng_parada, lat1, lon1)
            distancia_destino = distance(item.lat_parada, item.lng_parada, lat2, lon2)
            if distancia_origen < au_distancia_origen:
                parada_origen = item
                au_distancia_origen = distancia_origen
            if distancia_destino < au_distancia_destino:
                parada_destino = item
                au_distancia_destino = distancia_destino
    rutasorigen = Detalleparada.objects.filter(id_parada=parada_origen.id_parada).values()
    rutasdestino = Detalleparada.objects.filter(id_parada=parada_destino.id_parada).values()
    
    au_destino_id = parada_destino.id_parada
    au_origen_id = parada_origen.id_parada
    casea= 0
    exito= 0
    resultadodestino = rutasdestino
    resultadoorigen = rutasorigen
    for itemdestiny in rutasdestino:
        destino = itemdestiny
        for itemorigen in rutasorigen:
            origen = itemorigen
            if destino['id_recorrido_id'] == origen['id_recorrido_id']:
                casea= 1
                if destino['tiempo_marcha'] > origen['tiempo_marcha']:
                    exito = 1
    #Si tienen el mismo recorrido pero es vuelta no ida, ambas paradas estan mal
    if casea != 0 and exito != 1:
        weird = Detalleparada.objects.exclude(id_recorrido__id_recorrido__in = Detalleparada.objects.filter(id_parada__id_parada = au_destino_id).values_list('id_parada__id_parada', flat=True))
        wmenor = None
        wmenorDist = 0.0
        wdistancia = 0.0
        for itemweird in weird:
            orde = itemweird
            if wmenor == None:
                wmenor = orde
                wmenorDist = distance(orde.id_parada.lat_parada, orde.id_parada.lng_parada, lat1, lon1)
            else:
                wdistancia = distance(orde.id_parada.lat_parada, orde.id_parada.lng_parada, lat1, lon1)
                if wdistancia < wmenorDist:
                    wmenor = orde
                    wmenorDist = wdistancia
        tipo= 2
        parada_destino= wmenor
        au_destino_id= wmenor.id_parada.id_parada
        caseit= weird
        nuevo = None
        nuevo = Iteracion(caseit, au_destino_id, tipo, lat2, lon2)
        if nuevo != None:
            parada_origen= nuevo
            exito= 1
    #parada de origen esta bien y destino mal
    if exito != 1:
        nuevo = None
        itor = resultadodestino
        tipo= 2
        nuevo = Iteracion(itor, au_destino_id, tipo, lat2, lon2)
        if nuevo != None:
            parada_origen= nuevo
            exito= 1
    #parada de destino esta bien y origen mal
    if exito != 1:
        novo = None
        itdest = resultadoorigen
        tipo= 3
        novo = Iteracion(itdest, au_origen_id, tipo, lat2, lon2)
        if novo != None:
            parada_destino= novo
            exito= 1
    return parada_origen.id_parada.id_parada #parada_origen

def Iteracion(i_paradas, i_parada_id, i_tipo, i_lat, i_lon):
    i_exito = 0
    i_parada = None
    i_distance1 = i_distance2 = 0.0
    i_marcha_1 = i_marcha_2 = 0
    i_filter = Detalleparada.objects.filter(id_recorrido__id_recorrido__in = Detalleparada.objects.filter(id_parada__id_parada = i_parada_id).values_list('id_parada__id_parada', flat=True))
    for opcion_1 in i_paradas:
        i_marcha_1= opcion_1.tiempo_marcha
        for opcion_2 in i_filter:
            i_marcha_2= opcion_2.tiempo_marcha
            if i_parada == None:
                i_parada = opcion_2
                i_distance1 = distance(opcion_2.id_parada.lat_parada, opcion_2.id_parada.lng_parada, i_lat, i_lon)
                if i_tipo == 3 and i_marcha_1 > i_marcha_2:
                    i_exito= 1
                if i_tipo == 2 and i_marcha_2 > i_marcha_1:
                    i_exito= 1
            else:
                if i_tipo == 3 and i_marcha_1 > i_marcha_2:
                    i_distance2 = distance(opcion_2.id_parada.lat_parada, opcion_2.id_parada.lng_parada, i_lat, i_lon)
                    if i_distance2 < i_distance1:
                        i_parada = opcion_2
                        i_distance1 = i_distance2
                        i_exito= 1
                if i_tipo == 2 and i_marcha_2 > i_marcha_1:
                    i_distance2 = distance(opcion_2.id_parada.lat_parada, opcion_2.id_parada.lng_parada, i_lat, i_lon)
                    if i_distance2 < i_distance1:
                        i_parada = opcion_2
                        i_distance1 = i_distance2
                        i_exito= 1
    if i_exito != 0:
        return i_parada
    else:
        return None

def distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    
    # convert decimal degrees to radians 
    print(0)
    print(lat1)
    print(lon1)
    print(lat2)
    print(lon2)
    print(0)
    """
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)
    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km

















