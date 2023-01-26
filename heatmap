import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import os

#Pfad und Daten werden eingelesen
path=os.path.abspath(r'C:\Users\wiesbrock\Desktop\topview_femaleurineleft_39623_180722-convertedDLC_resnet50_Fabian_V1_TopviewMay18shuffle1_450000..xlsx')
data=pd.read_excel(path, header=None)

#Werte für die Position der Nase werden in Variablen überführt
snout_x=data[7]
snout_y=data[8]
snout_likelihood=data[9]

#Variablen werden zu Arrays umgewandelt, damit diese von matplotlib leichter zu verarbeiten sind
snout_x=np.array(snout_x)
snout_y=np.array(snout_y)

#Die ersten vier Reihen werden rausgenommen, da diese Infos enthalten, die wir nicht mehr brauchen

snout_x=snout_x[4:]
snout_y=snout_y[4:]

#Erstellung der Heatmap und Speicherung der normalisierten Position
h,x_edges,y_edges,mesh=plt.hist2d(snout_x,snout_y,bins=5, cmap='Greys')
h=np.transpose(h)

h=h/len(snout_x)

plt.hist2d(snout_x,snout_y,bins=5, cmap='Greys')
