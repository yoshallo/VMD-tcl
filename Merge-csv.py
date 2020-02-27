#Este es un script que combina dos archivos csv y que lo convierte en uno solo descartando una columna común. Útil para combinar dos salidas de funciones en función del tiempo por ejemplo.
import pandas as pd 
print('This is a script to merge two files in one, with the same first column name.')
file1=input('Please enter file name 1 \n ')
file2=input('Please enter file name 2 \n')
taitle=input('Please enter the key, or name of the common column. i.e. Time if a time dependent function')
oufile=input('Please enter your output file name')

a = pd.read_csv(file1)
b = pd.read_csv(file2)
b = b.dropna(axis=1)
merged = a.merge(b, on=taitle)
merged.to_csv(oufile+"output.csv", index=False)
