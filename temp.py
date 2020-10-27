# -*- coding: utf-8

#min (...)
#max (...)

import csv
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt

df = pd.read_csv("/Users/admin/Desktop/EIVP1/Semestre 1/Algorythme/Projet /EIVP_KM.csv",sep=';')
print (df)
#x = df ['noise' ] 
#y = df ['temp' ] 

x= df['noise'] 
y= df['temp']
plt.plot(df['noise'],df['temp'])
plt.show ()

plt.plot(x,y)

#EIVP_KM ['noise'].plot(kind'temp', tittle ='Noise Vs Temp')

        