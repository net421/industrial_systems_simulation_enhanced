
import random, os, csv

os.makedirs("../results", exist_ok=True)
SIM_TIME=5000

def simulate(rate):
    queues=[0,0,0]
    completed=0
    for t in range(SIM_TIME):
        queues[0]+=1
        for i in range(3):
            if queues[i]>0 and random.random()<rate[i]:
                queues[i]-=1
                if i<2:
                    queues[i+1]+=1
                else:
                    completed+=1
    return completed/SIM_TIME

results=[]
for b in [0.5,0.6,0.7]:
    th=simulate([1.0,0.8,b])
    results.append([b,th])

with open("../results/metrics.csv","w",newline="") as f:
    import csv
    writer=csv.writer(f)
    writer.writerow(["bottleneck","throughput"])
    writer.writerows(results)
