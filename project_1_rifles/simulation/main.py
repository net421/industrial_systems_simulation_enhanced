
import random, os, csv
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../results", exist_ok=True)

SIM_TIME = 5000

def simulate(lambda_rate, mu_rate):
    queue = 0
    completed = 0
    hist = []
    for t in range(SIM_TIME):
        if random.random() < lambda_rate:
            queue += 1
        if queue > 0 and random.random() < mu_rate:
            queue -= 1
            completed += 1
        hist.append(queue)
    return completed/SIM_TIME, np.mean(hist), hist

results = []
for mu in [0.8,1.0,1.2]:
    th, q, hist = simulate(0.9, mu)
    results.append([mu, th, q])
    plt.plot(hist)
    plt.title(f"Queue mu={mu}")
    plt.savefig(f"../results/queue_{mu}.png")
    plt.clf()

with open("../results/metrics.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["mu","throughput","avg_queue"])
    writer.writerows(results)
