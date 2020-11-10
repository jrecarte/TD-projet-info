import csv
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("C:\\Users\Paul\Documents\EIVP\TD-projet-info/EIVP_KM.csv",sep=';')


###Données d'entrées
datedépart= datetime.strptime(input("date de départ:"), "%Y-%m-%d")     #date de départ demandée
datearrivée= datetime.strptime(input("date d'arrivée:"), "%Y-%m-%d")    #date de fin demandée
NomDeLaDonnée = input("Nom de la donnée:")
NumCapteur = float(input("Quel capteur prendre:"))

###Indice humidex

def humidex(T):
    return(T + 5/9*(6.112*10*math.exp(7.5*((T)/(237.7+T)))*(T/100)-10))
Humidex=[]
for elt in df['temp']:
    Humidex.append(humidex(float(elt)))

###Tracé d'une donnée d'un capteur en fonction du temps

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

for i in range(len(capteur)):
    if capteur[i]!= NumCapteur:
        del DonnéeEtudiée[i]
        del date[i]


x = date                                                                #on affiche la courbe
y = DonnéeEtudiée
plt.plot(x,y)
plt.show()
