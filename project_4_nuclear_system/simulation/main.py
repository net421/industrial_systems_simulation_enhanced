
import os, csv
os.makedirs("../results", exist_ok=True)

years=range(1950,1990)
stock=0
data=[]
for y in years:
    if y<1960: p=50
    elif y<1970: p=300+(y-1960)*100
    elif y<1980: p=1200
    elif y<1986: p=1500
    else: p=-500
    stock+=p
    data.append([y,p,stock])

with open("../results/stock.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["year","production","stock"])
    writer.writerows(data)
