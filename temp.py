import csv
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from datetime import datetime

df = pd.read_csv("C:\\Users\Paul\Documents\EIVP\TD-projet-info/EIVP_KM.csv",sep=';')



###Indice humidex

def humidex(T,H):
    return(T + 5/9*(6.112*10**(7.5*((T)/(237.7+T)))*(H/100)-10))
Humidex=[]
for i in range(len(df['temp'])):
    Humidex.append(humidex(df['temp'][i],df['humidity'][i]))


action=sys.argv[0]
#####Affichage des courbes (display)
if action=="display" or action=="displayStat":
    variable=sys.argv[1]
    start_date=datetime.strptime(sys.argv[2], "%Y-%m-%d")
    end_date=datetime.strptime(sys.argv[3], "%Y-%m-%d")
    if action=="display":
        capteur=df['id']
        date = []
        if variable=='humidex':
            DonnéeEtudiée=Humidex
        else:
            DonnéeEtudiée=df[variable]

        for elt in df['sent_at']:
            date.append(datetime.strptime(elt[0:-6],"%Y-%m-%d %H:%M:%S"))




        for numcapteur in range(6):
            datef=[]
            DonnéeEtudiéef=[]
            for i in range(len(date)):
                if date[i]>=start_date and date[i]<=end_date and capteur[i]==numcapteur+1:
                    datef.append(date[i])
                    DonnéeEtudiéef.append(DonnéeEtudiée[i])
            if variable=="temp":
                variable="Température"
            elif variable=="noise":
                variable="bruit"
            elif variable=="humidity":
                variable="Humidité"
            elif variable=="lum":
                variable="Luminosité"

            titre="Tracé de "+ variable +" en fonction du temps " + "du capteur n°" + str(numcapteur+1)

            plt.figure(titre)
            plt.plot(datef,DonnéeEtudiéef,"b-",label=variable)
            plt.plot(datef,Moy,"c-.",label="Moyenne")
            plt.title(titre)
            plt.xlabel("Temps")
            plt.ylabel(variable)
            plt.legend()
        plt.show()
    ###Affichage des statistiques
    elif action=="displayStat":
        capteur=df['id']
        date = []
        if variable=='humidex':
            DonnéeEtudiée=Humidex
        else:
            DonnéeEtudiée=df[variable]

        for elt in df['sent_at']:
            date.append(datetime.strptime(elt[0:-6],"%Y-%m-%d %H:%M:%S"))

        for numcapteur in range(6):
            datef=[]
            DonnéeEtudiéef=[]
            for i in range(len(date)):
                if date[i]>=start_date and date[i]<=end_date and capteur[i]==numcapteur+1:
                    datef.append(date[i])
                    DonnéeEtudiéef.append(DonnéeEtudiée[i])
            ###Min-Max
            max=DonnéeEtudiéef[0]
            min=DonnéeEtudiéef[0]
            for i in range(len(DonnéeEtudiéef)):
                if DonnéeEtudiéef[i]<min:
                    min=DonnéeEtudiéef[i]
                if DonnéeEtudiéef[i]>max:
                    max=DonnéeEtudiéef[i]


            ###Moyenne
            if variable=="humidity":
                mult=1
                for elt in DonnéeEtudiéef:
                    mult*=elt/100
                moy=mult**(1/len(DonnéeEtudiéef))*100
            else:                #Pour l'humidité relative utilisé la moyenne géométrique, pour le reste, moyenne arithmétique
                somme=0
                for elt in DonnéeEtudiéef:
                    somme+=elt
                moy=somme/len(DonnéeEtudiéef)


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

            if variable=="temp":
                variable="Température"
            elif variable=="noise":
                variable="bruit"
            elif variable=="humidity":
                variable="Humidité"
            elif variable=="lum":
                variable="Luminosité"

            titre="Tracé de "+ variable +" en fonction du temps " + "du capteur n°" + str(numcapteur+1)
            Moy=[moy for i in range(len(DonnéeEtudiéef))]
            Max=[max for i in range(len(DonnéeEtudiéef))]
            Min=[min for i in range(len(DonnéeEtudiéef))]
            Var=[variance for i in range(len(DonnéeEtudiéef))]
            ET=[ecarttype for i in range(len(DonnéeEtudiéef))]
            Med=[médiane for i in range(len(DonnéeEtudiéef))]
            plt.figure(titre)
            plt.plot(datef,DonnéeEtudiéef,"b-",label=variable)
            plt.plot(datef,Moy,"c-.",label="Moyenne")
            plt.plot(datef,Max,"r:",label="Maximum")
            plt.plot(datef,Min,"g:",label="Minimum")
            # plt.plot(datef,Var)
            # plt.plot(datef,ET)
            plt.plot(datef,Med,"m--",label="Valeur médiane")
            plt.title(titre)
            plt.xlabel("Temps")
            plt.ylabel(variable)
            plt.legend()

        plt.show()



###Corrélation
elif action=="corrélation":
    variable1=sys.argv[1]
    variable2=sys.argv[2]
    start_date=datetime.strptime(sys.argv[3], "%Y-%m-%d")
    end_date=datetime.strptime(sys.argv[4], "%Y-%m-%d")


    ###Indice de corrélation
    """for i in range(len(variable1)):
        somme+=(variable1[i]-moyenne(variable1))*(variable2[i]-moyenne(variable2))
    covariance=somme*(1/len(variable1))
    indicecorr=covariance/(ecarttype(variable1)*ecarttype(variable2))
    """

