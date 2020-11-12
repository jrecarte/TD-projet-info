import csv
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("C:\\Users\Paul\Documents\EIVP\TD-projet-info/EIVP_KM.csv",sep=';')


###Données d'entrées
datedépart= datetime.strptime(input("date de départ:"), "%Y-%m-%d")    #date de départ demandée
datearrivée= datetime.strptime(input("date d'arrivée':"), "%Y-%m-%d")    #date de fin demandée
NomDeLaDonnée = input("Nom de la donnée:")
NumCapteur = float(input("Quel capteur prendre:"))

###Indice humidex
"""
def humidex(T):
    return(T + 5/9*(6.112*10*math.exp(7.5*((T)/(237.7+T)))*(T/100)-10))
Humidex=[]
for elt in df['temp']:
    Humidex.append(humidex(float(elt)))
"""
###Tracé d'une donnée d'un capteur en fonction du temps

capteur=df['id']
date = []
DonnéeEtudiée=df[NomDeLaDonnée]

for elt in df['sent_at']:                                               #on crée une liste des différentes dates sous le bon type : datetime
    date.append(datetime.strptime(elt[0:-6],"%Y-%m-%d %H:%M:%S"))


datef=[]
DonnéeEtudiéef=[]


for i in range(len(date)):
    if date[i]>=datedépart and date[i]<=datearrivée and capteur[i]==NumCapteur:
        datef.append(date[i])
        DonnéeEtudiéef.append(DonnéeEtudiée[i])

"""for elt in date:
    if elt<datetime.strptime(datedépart, "%Y-%m-%d"):
        DonnéeEtudiée.pop(date.index(elt))
        capteur.pop(date.index(elt))
        date.remove(elt)
    elif elt>datetime.strptime(datearrivée, "%Y-%m-%d"):
        DonnéeEtudiée.pop(date.index(elt))
        capteur.pop(date.index(elt))
        date.remove(elt)"""
max=DonnéeEtudiéef[0]
min=DonnéeEtudiéef[0]
for i in range(len(DonnéeEtudiéef)):
    if DonnéeEtudiéef[i]<min:
        min=DonnéeEtudiéef[i]
    if DonnéeEtudiéef[i]>max:
        max=DonnéeEtudiéef[i]


sum=0                                                                           #la moyenne est terrible faut en utiliser une autre
for elt in DonnéeEtudiéef:
    sum+=elt
moy=sum/len(DonnéeEtudiéef)



Moy=[moy for i in range(len(DonnéeEtudiéef))]
Max=[max for i in range(len(DonnéeEtudiéef))]
Min=[min for i in range(len(DonnéeEtudiéef))]                                   #on affiche la courbe
plt.plot(datef,DonnéeEtudiéef)
plt.plot(datef,Moy)
plt.plot(datef,Max)
plt.plot(datef,Min)
plt.show()
