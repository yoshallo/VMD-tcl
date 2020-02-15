import pandas as pd
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askdirectory
import csv
import os


print('This is a Python script to read *.psf topology files and *.dcd coordinates from molecular dynamics obtained from NAMD using VMD. \n In order to obtain Radius of Gyration (RoG) ')
print('Please enter your base filename e.g. if your psf file is dynamics1.a.0.psf, \n please enter the first part <dynamics1> without extension')
#basename=askopenfile()
basedyn=input("Please enter your base file name: \n")
#systename=input("Please enter your system name, if you are working with specific protein or structures: \n")
steps=input("If your dynamic is too long, please enter the steps to read coordinates files (suggested: 10): \n")
ofname=input("Name of your out file")
#print("Now please, enter the system to measure RoG: \n")
#rmeasure=input("(protein, chain, name CA, resid x to y): \n ")
f = open("RadOfGyr.tcl", "w")
f.write("""
#Para listar los archivos de trayectoria
glob *.coor.dcd
set files [glob *.coor.dcd]
set list [lsort $files]
foreach i $list {
mol addfile "$i" first 0 step """+steps+""" waitfor all
}



puts -nonewline " Select yout systemr (e.g protein, name CA, resid number etc.): "
gets stdin selmode
set sel [atomselect top "$selmode"]
###the above is to select atoms. input format should be "resname SSH " and the like.


set outf [open """+ofname+""".csv w]
#get number of frames
set n [molinfo top get numframes]
###set up output file name.
puts $outf Time,RoG
for {set i 0} {$i < $n} {incr i} {
molinfo top set frame $i
set radgyr [measure rgyr $sel]
puts $outf $i\,$radgyr
}
close $outf

exit""")
f.close()
os.system("vmd -dispdev text "+basedyn+".a.0.psf -e RadOfGyr.tcl exit")

#filename1 = askopenfile()
plottitle = input('Please enter your system name, (e.g. Methotrexate-Folate Reductase): \n')
xaxislabel = input('Please enter X axis label: \n ')
yaxislabel = input('Please enter Y axis label: \n ')
#print('What are you going to plot? (RMSD, RMSF, RoG) \n')
vartoplot = pd.read_csv(ofname+".csv", index_col=0)
#vartoplot = pd.read_csv(basename+'_RadOfGyr.csv', index_col=0)
#vartoplot.plot()

plot = vartoplot.plot(title=' '+plottitle+' ', lw=2, colormap='jet', marker='x', markersize=10)
plot.set_xlabel(' '+xaxislabel+' ')
plot.set_ylabel(' '+yaxislabel+' ')
plt.show()
