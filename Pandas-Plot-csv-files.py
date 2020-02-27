#######Plot-csv.py                                                                                                   

import pandas as pd
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename 
from tkinter.filedialog import askdirectory    

print('Make sure your file contains Headers per columnns and an adequate separator character e.g , \n ')
#filename1=input('Please enter your file name with extension, e.g. HelloWorld.csv \n')
filename1 = askopenfilename()
plottitle = input('Please enter your system name, (e.g. Methotrexate-Folate Reductase): \n')
xaxislabel = input('Please enter X axis label: \n ')
yaxislabel = input('Please enter Y axis label: \n ')
#print('What are you going to plot? (RMSD, RMSF, RoG) \n')

vartoplot = pd.read_csv(filename1, index_col=0)
#vartoplot.plot()

plot = vartoplot.plot(title=' '+plottitle+' ', lw=1.0, colormap='jet', marker='.', markersize=2.2, fontsize=30)
plt.legend(fontsize=20)
plot.set_xlabel(' '+xaxislabel+' ', fontsize=24)
plot.set_ylabel(' '+yaxislabel+' ', fontsize=24)
plt.show()
