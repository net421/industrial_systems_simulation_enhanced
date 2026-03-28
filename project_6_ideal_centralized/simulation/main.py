import os, csv
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../results", exist_ok=True)

SIM_TIME = 5000

def real_system(rates):
    queues = [0, 0, 0]
    completed = 0
    history = []

    for t in range(SIM_TIME):
        queues[0] += 1
        for i in range(3):
            if queues[i] > 0 and np.random.rand() < rates[i]:
                queues[i] -= 1
                if i < 2:
                    queues[i+1] += 1
                else:
                    completed += 1
        history.append(sum(queues))

    throughput = completed / SIM_TIME
    avg_wip = np.mean(history)
    return throughput, avg_wip, history

def ideal_system(rate):
    completed = 0
    history = []

    for t in range(SIM_TIME):
        if np.random.rand() < rate:
            completed += 1
        history.append(0)

    throughput = completed / SIM_TIME
    avg_wip = 0
    return throughput, avg_wip, history

results = []

bottlenecks = [0.5, 0.6, 0.7]

for b in bottlenecks:
    real_th, real_wip, real_hist = real_system([1.0, 0.8, b])
    ideal_th, ideal_wip, ideal_hist = ideal_system(b)

    results.append([b, real_th, ideal_th, real_wip, ideal_wip])

with open("../results/comparison.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["bottleneck","real_throughput","ideal_throughput","real_wip","ideal_wip"])
    writer.writerows(results)

b_vals = [r[0] for r in results]
real_vals = [r[1] for r in results]
ideal_vals = [r[2] for r in results]

plt.plot(b_vals, real_vals, label="Real System")
plt.plot(b_vals, ideal_vals, label="Ideal System")
plt.xlabel("Bottleneck Rate")
plt.ylabel("Throughput")
plt.legend()
plt.title("Real vs Ideal Centralized System")

plt.savefig("../results/comparison.png")
plt.close()

print("Experiment completed. Check results folder.")
