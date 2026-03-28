
import random, os, csv

os.makedirs("../results", exist_ok=True)
SIM_TIME=5000

def simulate(n):
    total=0
    for t in range(SIM_TIME):
        for _ in range(n):
            if random.random()<0.6:
                total+=1
    return total/SIM_TIME

results=[]
for n in [1,2,5,10]:
    th=simulate(n)
    results.append([n,th])

with open("../results/metrics.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["factories","throughput"])
    writer.writerows(results)
