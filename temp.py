import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys
from datetime import datetime

df = pd.read_csv("C:\\Users\Paul\Documents\EIVP\TD-projet-info/EIVP_KM.csv",sep=';')



###Indice humidex

def humidex(T,H):
    return(T + 5/9*(6.112*10**(7.5*((T)/(237.7+T)))*(H/100)-10))
Humidex=[]
for i in range(len(df['temp'])):
    Humidex.append(humidex(df['temp'][i],df['humidity'][i]))

def moyenne(variable,donnéeEtudiée):
    if variable=="humidity":
        mult=1
        for elt in donnéeEtudiée:
            mult*=elt/100
        return(mult**(1/len(donnéeEtudiée))*100)
    else:
        somme=0
        for elt in donnéeEtudiée:
            somme+=elt
        return(somme/len(donnéeEtudiée))
def ecarttype(variable,DonnéeEtudiée):
    somme=0
    for elt in DonnéeEtudiée:
        somme+=(elt-moyenne(variable,DonnéeEtudiée))**2
    variance=somme/len(DonnéeEtudiée)
    return(variance**0.5)





action=sys.argv[1]
if action=="display" or action=="displayStat":
    variable=sys.argv[2]
    start_date=datetime.strptime(sys.argv[3], "%Y-%m-%d")
    end_date=datetime.strptime(sys.argv[4], "%Y-%m-%d")
    ###DISPLAY (AFFICHAGE DE COURBES)
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
    variable1=sys.argv[2]
    variable2=sys.argv[3]
    start_date=datetime.strptime(sys.argv[4], "%Y-%m-%d")
    end_date=datetime.strptime(sys.argv[5], "%Y-%m-%d")
    capteur=df['id']
    date = []

    for elt in df['sent_at']:
        date.append(datetime.strptime(elt[0:-6],"%Y-%m-%d %H:%M:%S"))

    if variable1=='humidex':
        DonnéeEtudiée1=Humidex
    else:
        DonnéeEtudiée1=df[variable1]
    if variable2=='humidex':
        DonnéeEtudiée2=Humidex
    else:
        DonnéeEtudiée2=df[variable2]


    for numcapteur in range(6):
        datef=[]
        DonnéeEtudiée1f=[]
        DonnéeEtudiée2f=[]
        for i in range(len(date)):
            if date[i]>=start_date and date[i]<=end_date and capteur[i]==numcapteur+1:
                datef.append(date[i])
                DonnéeEtudiée1f.append(DonnéeEtudiée1[i])
                DonnéeEtudiée2f.append(DonnéeEtudiée2[i])


        somme=0
        for i in range(len(DonnéeEtudiée1f)):
            somme+=(DonnéeEtudiée1f[i]-moyenne(variable1,DonnéeEtudiée1f))*(DonnéeEtudiée2f[i]-moyenne(variable2,DonnéeEtudiée2f))
        covariance=somme*(1/len(DonnéeEtudiée1f))
        indicecorr=covariance/(ecarttype(variable1,DonnéeEtudiée1f)*ecarttype(variable2,DonnéeEtudiée2f))
        indicecorrstr=str(indicecorr)

        if variable1=="temp":
            variable1="Température"
        elif variable1=="noise":
            variable1="bruit"
        elif variable1=="humidity":
            variable1="Humidité"
        elif variable1=="lum":
            variable1="Luminosité"
        if variable2=="temp":
            variable2="Température"
        elif variable2=="noise":
            variable2="bruit"
        elif variable2=="humidity":
            variable2="Humidité"
        elif variable2=="lum":
            variable2="Luminosité"


        titre="Tracé de "+ variable1 + " et de " + variable2 + " en fonction du temps " + "du capteur n°" + str(numcapteur+1) + ". Les variables ont alors un indice de corrélation de " + str(indicecorr)[0:4]
        fig, ax1 = plt.subplots()

        color = 'tab:red'
        ax1.set_xlabel('Temps')
        ax1.set_ylabel(variable1, color=color)
        ax1.plot(datef, DonnéeEtudiée1f, color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()
        color = 'tab:blue'
        ax2.set_ylabel(variable2, color=color)
        ax2.plot(datef, DonnéeEtudiée2f, color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()
        plt.title(titre)
    plt.show()