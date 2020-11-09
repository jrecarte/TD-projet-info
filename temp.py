import csv
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("C:\\Users\Paul\Documents\EIVP\TD-projet-info/EIVP_KM.csv",sep=';')
datedépart= datetime.strptime(input("date de départ:"), "%Y-%m-%d")     #date de départ demandée
datearrivée= datetime.strptime(input("date d'arrivée:"), "%Y-%m-%d")    #date de fin demandée
NomDeLaDonnée = input("Nom de la donnée:")
NumCapteur = float(input("Quel capteur prendre:"))
capteur=df['id']
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
<<<<<<< HEAD
for i in range(len(capteur)):
    if capteur[i]!= NumCapteur:
        del DonnéeEtudiée[i]
        del date[i]
=======
>>>>>>> b2cef6a6b9d250bbc41719df3bf71a64a58f7f58

x = date                                                                #on affiche la courbe
y = DonnéeEtudiée
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


#calcul indice humidex

import math                                            
def humidex (T):                                              #je définis ma fonction "humidex" à créer, elle dépend du paramètre T ou température (à voir si c'est nécessaire de l'appeler T plutot que température )
    H= humidex ('temp')                                       #je la nomme "H" pour la suite
               for T in range(df['temp']))                    #j'utilise les donnés de la température dans le CSV et je nomme la variable "T"
               H= T + 5/9*(6,112*10exp(7,5*((T)/(237,7+T)))*('T/100)-10      #formule humidex avec une seule variable T
    return humidex              #return pour terminer les détails de la fonction

print humidex              #j'affiche les résultats, comment on fait pour ajouter une nouvelle colonne avec ces résultats ?

x = df['humidex']                                                        #on affiche la courbe
y = df['date']         #avec ce que tu as modifié, comment on fait pour récupérer le temps (différence avec les dates)
plt.plot(x,y)
plt.show()
=======



"""
def get_humidex(t, d):

    kelvin = 273.15
    temperature = t + kelvin
    dewpoint = d + kelvin

    # Calculate vapor pressure in mbar.
    e = 6.11 * math.exp(5417.7530 * ((1 / kelvin) - (1 / dewpoint)))

    # Calculate saturation vapor pressure
    h = 0.5555 * (e - 10.0)

    humidex = temperature + h - kelvin

=======

#humidex=[]                #c'était ce que tu avais ajouté toi il me semble de ton côté, quand on avait discuté ensemble l'autre jour
#for i in range(len(df['temp'])):
    #humidex.append(get_humidex(df['temp'], df['humidity']))
=======
for i in range(len(df['temp'])):
    humidex.append(get_humidex(df['temp'], df['humidity']))"""
>>>>>>> 0843049dcf3433cf45408c1b1a8d74d638721424
