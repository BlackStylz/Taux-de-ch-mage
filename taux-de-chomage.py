import pandas as pd
import matplotlib.pyplot as plt


unrate = pd.read_csv("unrate.csv")
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(10,6))
colors = ['red','blue','green','orange','black']

for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'],subset['UNRATE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title('Evolution du taux de chômage de 1948 à 1952')
plt.xlabel('Mois (de 1 à 12)')
plt.ylabel('Taux de chômage (en %)')
plt.show()
