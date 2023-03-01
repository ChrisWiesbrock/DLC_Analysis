import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import os

#Pfad und Daten werden eingelesen
path=os.path.abspath(r'C:\Users\wiesbrock\Desktop\2_Cam_Frizi-220630-125958_725_DREADD-220709-134115_Cam1DLC_resnet50_Frizi_MaLabDataDec19shuffle1_450000.csv')
data=pd.read_csv(path,delimiter=';',header=None)
#data=pd.read_csv(path,delimiter=',',header=None)
num_bin=5

#Werte für die Position der Nase werden in Variablen überführt
snout_x=data[7]
snout_y=data[8]
snout_likelihood=data[9]

#Variablen werden zu Arrays umgewandelt, damit diese von matplotlib leichter zu verarbeiten sind
snout_x=np.array(snout_x)
snout_y=np.array(snout_y)

#Die ersten vier Reihen werden rausgenommen, da diese Infos enthalten, die wir nicht mehr brauchen

snout_x=snout_x[4:].astype(float)
snout_y=snout_y[4:].astype(float)

#Erstellung der Heatmap und Speicherung der normalisierten Position
h,x_edges,y_edges,mesh=plt.hist2d(snout_x,snout_y,bins=num_bin, cmap='Greys')
h=np.transpose(h)

h=h/len(snout_x)

plt.hist2d(snout_x,snout_y,bins=num_bin, cmap='Greys')
