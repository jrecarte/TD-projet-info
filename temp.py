import csv
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("C:\\Users\Paul\Documents\EIVP\Projet Python/EIVP_KM.csv",sep=';')
datedépart= datetime.strptime(input("date de départ:"), "%Y-%m-%d")     #date de départ demandée
datearrivée= datetime.strptime(input("date d'arrivée:"), "%Y-%m-%d")    #date de fin demandée
NomDeLaDonnée = input("Nom de la donnée:")
date = []
DonnéeEtudiée=df[NomDeLaDonnée]

for elt in df['sent_at']:                                               #on crée une liste des différentes dates sous le bon type : datetime
    date.append(datetime.strptime(elt[0:-6],"%Y-%m-%d %H:%M:%S"))
for elt in date:                                                        #on prend les dates pour quelles soient comprises entre la date de départ et celle de fin ET c'est là qu'est le
    if elt<datedépart:                                                  #problème
        DonnéeEtudiée.pop(date.index(elt))
        date.remove(elt)
    elif elt>datearrivée:
        DonnéeEtudiée.pop(date.index(elt))
        date.remove(elt)
x = date                                                                #on affiche la courbe
y = df['noise']
plt.plot(x,y)
plt.show()


"""
def convtime(strtime):
    Convert a date "YYYY-MM-DD" as a time since EPOCH.
    listtime = strtime.strip('-')
    tupletime = (listtime[0], listtime[1], listtime[2])

    # datetime.datetime.fromtimestamp(tupletime)
    # Cette fonction fait l'inverse de ce que j'attends...

    return time

time deltatime ()"""



#calcul indice humidex. il manque l'utilisation de nos données, je m'en occupe ce weekend.

# t is temperature in °C
# d is dew Point Temperature in °C
import math


def get_humidex(t, d):

    kelvin = 273.15
    temperature = t + kelvin
    dewpoint = d + kelvin

    # Calculate vapor pressure in mbar.
    e = 6.11 * math.exp(5417.7530 * ((1 / kelvin) - (1 / dewpoint)))

    # Calculate saturation vapor pressure
    h = 0.5555 * (e - 10.0)

    humidex = temperature + h - kelvin

    return humidex
humidex=[]
for i in range(len(df['temp'])):
    humidex.append(get_humidex(df['temp'], df['humidity']))
