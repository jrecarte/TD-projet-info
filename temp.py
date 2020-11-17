import csv
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("C:\\Users\Paul\Documents\EIVP\TD-projet-info/EIVP_KM.csv",sep=';')



###Indice humidex

def humidex(T,H):
    return(T + 5/9*(6.112*10**(7.5*((T)/(237.7+T)))*(H/100)-10))
Humidex=[]
for i in range(len(df['temp'])):
    Humidex.append(humidex(df['temp'][i],df['humidity'][i]))



###Données d'entrées

datedépart= datetime.strptime(input("date de départ:"), "%Y-%m-%d")    #date de départ demandée
datearrivée= datetime.strptime(input("date d'arrivée':"), "%Y-%m-%d")    #date de fin demandée
NomDeLaDonnée = input("Nom de la donnée:")
NumCapteur = float(input("Quel capteur prendre:"))




###Tracé d'une donnée d'un capteur en fonction du temps

capteur=df['id']
date = []
if NomDeLaDonnée=='humidex':
    DonnéeEtudiée=Humidex
else:
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


###Min-Max
max=DonnéeEtudiéef[0]
min=DonnéeEtudiéef[0]
for i in range(len(DonnéeEtudiéef)):
    if DonnéeEtudiéef[i]<min:
        min=DonnéeEtudiéef[i]
    if DonnéeEtudiéef[i]>max:
        max=DonnéeEtudiéef[i]


###Moyenne
if NomDeLaDonnée=="humidity":
    mult=1
    for elt in DonnéeEtudiéef:
        mult*=elt/100
    moy=mult**(1/len(DonnéeEtudiéef))*100
else:                #Pour l'humidité relative utilisé la moyenne géométrique, pour le reste, moyenne arithmétique
    sum=0
    for elt in DonnéeEtudiéef:
        sum+=elt
    moy=sum/len(DonnéeEtudiéef)


###Variance
somme=0
for elt in DonnéeEtudiéef:
    somme+=(elt-moy)**2                      #on ne peut que si la donnée n'est pas l'humidity n'est ce pas ?
variance=somme/len(DonnéeEtudiéef)
ecarttype=variance**0.5

###Médiane
DonnéeTriée=sorted(DonnéeEtudiéef)
index=(len(DonnéeTriée)-1)//2
if len(DonnéeTriée)%2==1:
    médiane=DonnéeTriée[index]
else:
    médiane=(DonnéeTriée[index]+DonnéeTriée[index+1])/2

###Nom pour graphique
if NomDeLaDonnée=="temp":
    NomDeLaDonnée="Température"
elif NomDeLaDonnée=="noise":
    NomDeLaDonnée="bruit"
elif NomDeLaDonnée=="humidity":
    NomDeLaDonnée="Humidité"
elif NomDeLaDonnée=="lum":
    NomDeLaDonnée="Luminosité"

titre="Tracé de "+ NomDeLaDonnée +" en fonction du temps"

Moy=[moy for i in range(len(DonnéeEtudiéef))]
Max=[max for i in range(len(DonnéeEtudiéef))]
Min=[min for i in range(len(DonnéeEtudiéef))]
Var=[variance for i in range(len(DonnéeEtudiéef))]
ET=[ecarttype for i in range(len(DonnéeEtudiéef))]
Med=[médiane for i in range(len(DonnéeEtudiéef))]
plt.plot(datef,DonnéeEtudiéef,"b-",label=NomDeLaDonnée)
plt.plot(datef,Moy,"c-.",label="Moyenne")
plt.plot(datef,Max,"r:",label="Maximum")
plt.plot(datef,Min,"g:",label="Minimum")
# plt.plot(datef,Var)
# plt.plot(datef,ET)
plt.plot(datef,Med,"m--",label="Valeur médiane")
plt.title(titre)
plt.xlabel("Temps")
plt.ylabel(NomDeLaDonnée)
plt.legend()
plt.show()
