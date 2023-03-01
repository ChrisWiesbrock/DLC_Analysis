# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:46:17 2023

@author: wiesbrock
"""

import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import scipy.stats as stats
import glob
from scipy.signal import argrelextrema
import pandas as pd
import os


#Pfad und Daten werden eingelesen
path=os.path.abspath(r'C:\Users\wiesbrock\Desktop\2_Cam_Frizi-220630-125958_725_DREADD-220709-134115_Cam1DLC_resnet50_Frizi_MaLabDataDec19shuffle1_450000.csv')
data=pd.read_csv(path,delimiter=';',header=None)
#data=pd.read_csv(path,delimiter=';',header=None)

def distance(x2,x1,y2,y1):
    dist = np.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return dist


#Werte für die Position der Nase werden in Variablen überführt
snout_x=data[10]
snout_y=data[11]
snout_likelihood=data[12]

#Variablen werden zu Arrays umgewandelt, damit diese von matplotlib leichter zu verarbeiten sind
snout_x=np.array(snout_x)
snout_y=np.array(snout_y)


#Die ersten vier Reihen werden rausgenommen, da diese Infos enthalten, die wir nicht mehr brauchen

snout_x=snout_x[4:].astype(float)
snout_y=snout_y[4:].astype(float)

#Filter anhand der Likelihood um grobes Misstracking rauszufiltern
snout_likelihood=snout_likelihood[4:].astype(float)
snout_x=snout_x[snout_likelihood>0.95]
snout_y=snout_y[snout_likelihood>0.95]


distance_values=np.zeros((len(snout_x),1))
for i in range(len(snout_x)-1):
    distance_values[i]=distance(snout_x[i+1],snout_x[i],snout_y[i+1],snout_y[i])



#40 cm = 345 pixel
#1cm = 8,625 pixel
#20 fps
#1 Value = 1/20 sec

for i in range(len(distance_values)):
    distance_values[i]=(distance_values[i]*20)/8.625
    
distance_values=distance_values[distance_values<50]
hist,edges=np.histogram(distance_values)
sns.distplot(distance_values)
plt.ylabel('Speed [cm/s]')
plt.figure()
plt.plot(snout_x,snout_y)
plt.xlabel('x_position [pixel]')
plt.ylabel('y_position [pixel]')


    
