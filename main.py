import pandas as pd
import numpy as np

df = pd.read_csv("french_dictionary.csv")
x = df["eng"]
y = df["french"]

fin = open("t8.shakespeare.txt", "rt")
fout = open("out.txt", "wt")

k = 0
while(k < 1000):
    for line in fin:
	    fout.write(line.replace(x[k], y[k]))
    k = k + 1    

fin.close()
fout.close()