import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os
#HOLO
basedyn=input("Tira el nombre base de la dinamica: ")
#archivo=input("Tira el nombre de tu archivo otra vez...")

f = open("RMSD.tcl", "w")
f.write("""
puts "Steps para leer dinamica:	"
gets stdin steps
puts "Sistema para el cual calcular RMSD."
puts "protein, chain, name CA, resid	"
gets stdin sistema
set files [glob *.coor.dcd]
set list [lsort $files]
foreach i $list {
mol addfile "$i" first 0 step $steps waitfor all
} 
set outfile [open """+basedyn+"""_RMSD.csv w]
set nf [molinfo top get numframes]
set frame0 [atomselect top $sistema frame 0]
set sel [atomselect top $sistema]
# rmsd calculation loop
for { set i 0 } { $i <= $nf } { incr i } {
$sel frame $i
$sel move [measure fit $sel $frame0]
puts $outfile "[expr {$i+1}]\,[measure rmsd $sel $frame0]"
}
close $outfile
exit""")

f.close()

os.system("vmd -dispdev text "+basedyn+".a.0.psf -e RMSD.tcl")

#filename1 = askopenfile()
plottitle = input('Please enter your system name, (e.g. Methotrexate-Folate Reductase): \n')
xaxislabel = input('Please enter X axis label: \n ')
yaxislabel = input('Please enter Y axis label: \n ')
#print('What are you going to plot? (RMSD, RMSF, RoG) \n')
vartoplot = pd.read_csv(basedyn+"_RMSD.csv", index_col=0)
#vartoplot = pd.read_csv(basename+'_RadOfGyr.csv', index_col=0)
#vartoplot.plot()

plot = vartoplot.plot(title=' '+plottitle+' ', lw=2, colormap='jet', marker='x', markersize=10)
plot.set_xlabel(' '+xaxislabel+' ')
plot.set_ylabel(' '+yaxislabel+' ')
plt.show()
