import numpy as np 
import pandas as pd
import subprocess

f=pd.read_csv("DOI")
vals=f.values.tolist()

for i in range (len(vals)):
    subprocess.run("scidownl download --doi https://doi.org/"+str(vals[i][0])+"--out "+str(i),shell=True)
