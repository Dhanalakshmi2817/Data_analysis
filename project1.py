# -*- coding: utf-8 -*-
"""Project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11DYTpfVU38Lfi_IVDokYdG3avSVd9i41
"""

# calculating maximum,minimum,average and certain threshold tempreature
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
d=pd.read_excel("/content/Book1.xlsx")
print(d)
print("Average temperature")
v=d['Temp'].mean()
print(v)
print("Maximum temperature")
c=np.max(d['Temp'])
print(c)
print("Minimum temperature")
e=np.min(d['Temp'])
print(e)
plt.plot(d['Day'],d['Temp'],color='Hotpink',marker='.')
plt.title('Temperature analysis(deg celsius)')
plt.xlabel('Day')
plt.ylabel('Temperature')
temperature_threshold = 25
high_temp_days = d[d['Temp'] > temperature_threshold].shape[0]
print(f"Number of days where the temperature exceeded {temperature_threshold}°C: {high_temp_days} days")
plt.show()