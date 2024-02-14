# -*- coding: utf-8 -*-
"""DAP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A-9I-ARqZS5FmfcjN8YCUtVW0ACNHbK6
"""

import numpy as np
# creating arrays
arr =np.array([1,2,3,4,5])
print(arr)
a=np.zeros((3,3),dtype=int)
print(a)
b=np.ones((2,2),dtype=int)
print(b)
c=np.arange(10)
print(c)
# Array manipulation
d=arr.reshape(5,1)
print(d)
# sliced array
e=arr[2:4]
print(e)
#stacking array vertically
a=np.array([1,2,3])
b=np.array([5,6,7])
c=np.vstack(a+b)
print(c)
a=np.array([1,2,3])
b=np.array([5,6,7])
c=np.stack(a+b)
print(c)

# Addition of two arrays
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
print(arr1+arr2)
#broadcasting
arr1=np.array([1,2,3,4,5])
print(arr1+3)
#split
arr2=np.array([1,2,3,4,5,6])
b=np.split(arr2,3)
print(b)
# Transposing the array
a= np.array([[1,3],
            [2,4]])
b=a.T
print(b)

# Dot product
a= np.array([[1,3],[2,4]])
b=np.array([[5,6],[7,8]])
c=np.dot(a,b)
print(c)
# calculating eigen value and eigen vector
d=np.linalg.eig(c)
print(d)

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[9,2,3],[5,2,4]])
result=np.sum(a)
result2=np.sum(a,axis=0)#row wise matrix addition
result3=np.sum(a,axis=1)#column wise matrix addition
print(result3)
print(result2)
print(result)
result1=np.sum(a+b)
print(result1)
#statistical operations
v=np.array([1,2,3,4,5])
v1=np.mean(v)
v2=np.median(v)
v3=np.var(v)
v4=np.std(v)
print(v1)
print(v2)
print(v3)
print(v4)

#creating and loading a data set
data=np.loadtxt("/content/number.txt")
print(data)
data1=np.loadtxt("/content/number.txt",dtype=int)
print(data1)
data2=np.savetxt("/content/number",data)
print(data2)

#plotting data methods
import matplotlib.pyplot as plt
a=np.array([1,2,3,4,5,6,7,8,9,10])
plt.plot(a)

# importing pandas
import pandas as pd
a=["Dhana",'Vasanthi','Lalitha','Lahari','Yamini','Sunny','Bhargav']
r=pd.Series(a,index=[67,43,44,89,34,45,23])
print(r)
#uploading csv files using pandas
a=pd.read_csv("/content/apple_quality.csv")
print(a)
print(a.loc[1])
print(a.loc[6:7])
b=a['Size'].mean()
a=a.fillna(b)
print(a)
a=a.drop_duplicates()
print(a)
a.shape

# .txt file
a=pd.read_csv("/content/n.txt",sep=" ")
print(a)
# xlsx file
a=pd.read_excel("/content/Historicalinvesttemp.xlsx",sheet_name=0)
print(a)
a.shape

a=pd.read_csv("/content/apple_quality.csv")
a.head()
a.shape

a=pd.read_csv("/content/apple_quality.csv")
a.shape
testing=a.tail(10)
for i in range(4000,3990,-1):
  a.drop([i],axis=0,inplace=True)
  testing.to_csv("manual_testing.csv")
print(testing.groupby(['Sweetness'])['Crunchiness'].count())

# plotting
import numpy as np
import matplotlib.pyplot as plt
runs=np.array([100,50,91,78,89,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.scatter(runs,w,color='pink')
plt.title('IndvsAus_score')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
# Generate array of 200 values between pi and -pi
tigar=np.linspace(-2*np.pi,2*np.pi,50)
print(tigar)
plt.plot(tigar,np.sin(tigar),color='black')
#plt.plot(x,y,,color,labels....)
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
# creating x
overs=np.arange(5,50,5)
overs_a=np.arange(5,30,5)
# creating y
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,110,151])
wickets=np.array([12,32,96])
# plotting
plt.plot(overs,runs_i,color='blue',label='India')
plt.plot(overs_a,runs_a,color='yellow',label='Aus')
# combining two graphs
plt.legend(loc='best')
# displaying the final graph
plt.show()

# SUB PLOT
import numpy as np
import matplotlib.pyplot as plt
# creating x
overs=np.arange(5,50,5)
overs_a=np.arange(5,30,5)
# creating y
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,110,151])
wickets=np.array([12,32,96])
# plotting
plt.subplot(2,1,2)
plt.plot(overs,runs_i,color='blue',label='India')
plt.legend(loc='best')
plt.subplot(2,1,1)
plt.plot(overs_a,runs_a,color='yellow',label='Aus')
# combining two graphs
plt.legend(loc='best')
# displaying the final graph
plt.show()

import matplotlib.pyplot as plt
a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]
profit_a=[(a[i]-a[i-1]) for i in range (1,len(a))]
profit_b=[(b[i]-b[i-1]) for i in range (1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='hotpink',linewidth='3',label='CompanyA',marker='>',ms='15',mec='k')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='black',linestyle='dotted',label='CompanyB',marker='H')

a=np.array([25,60,5,10])
labe=["AIML","Python","Pandas","Numpy"]
colors=['Green','Hotpink','Pink','Yellow']
plt.pie(a,labels=labe,colors=colors)
plt.show()

# explode
a=np.array([25,60,5,10])
labe=["AIML","Python","Pandas","Numpy"]
colors=['Hotpink','BLue','Pink','Yellow']
sizes=[18,18,18,18]
fontsize = 20
explo=[0.2,0,0,0]
plt.pie(a,labels=labe,explode=explo,colors=colors,startangle=180,textprops={'fontsize':fontsize},shadow='true' )
plt.show()

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

pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
# load example dataset
tips=sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",data=tips)
plt.title("Scatter plot of total bill vs.Tip")
plt.xlabel("Total Bill($)")
plt.ylabel("Tip($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
# load example dataset
tips=sns.load_dataset("titanic")
print(tips.head(5))
sns.scatterplot(x="survived",y="age",data=tips)
plt.title("Scatter plot of survived vs.Age")
plt.xlabel("survived ($)")
plt.ylabel("Tip ($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
# load example dataset
tips=sns.load_dataset("titanic")
print(tips.head(5))
sns.violinplot(x="survived",y="age",data=tips)
plt.title("Scatter plot of survived vs.Age")
plt.xlabel("survived ($)")
plt.ylabel("Tip ($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")
print(iris)
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap of Iris Dataset")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("diamonds")
print(iris)
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap of Iris Dataset")
plt.show()