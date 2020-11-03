# -*- coding: utf-8

#min (...)
#max (...)

import csv
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt

df = pd.read_csv("/Users/admin/Documents/GitHub/Projet_INFO/EIVP_KM.csv",sep=';')
print (df)
#x = df ['noise' ] 
#y = df ['temp' ] 

x = df['noise'] 
y = df['temp']
plt.plot(df['noise'],df['temp'])
plt.show ()

plt.plot(x,y)

#EIVP_KM ['noise'].plot(kind'temp', tittle ='Noise Vs Temp')

def convtime(strtime):
    """Convert a date "YYYY-MM-DD" as a time since EPOCH."""
    listtime = strtime.strip('-')
    tupletime = (listtime[0], listtime[1], listtime[2])
 
    # datetime.datetime.fromtimestamp(tupletime)
    # Cette fonction fait l'inverse de ce que j'attends...
 
    return time

time deltatime ()

