
import os, numpy as np, csv
os.makedirs("../results", exist_ok=True)

A=np.array([[0.2,0.1],[0.05,0.3]])
d=np.array([100,150])
x=np.linalg.inv(np.eye(2)-A).dot(d)

with open("../results/output.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["sector1","sector2"])
    writer.writerow(x)
