
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset
DataFrame=pd.read_csv('carsss.csv')

#creating boxplot on a single graph
np.random.seed(1234)

df=pd.DataFrame(np.random.randn(10,5),
                columns=['SP','WT','HP','VOL','MPG'])
boxplot=df.boxplot(column=['SP','WT','HP','VOL','MPG'])

#calculating IQRs:
sorted(DataFrame['MPG'])
q1,q3= np.percentile (DataFrame['MPG'], [25,75]) #q1=27.85 #q3=39.531
iqr=q3-q1 #11.67

lower_bound= (q1-1.5*iqr) #10.343
upper_bound= (q3+1.5*iqr) #57.044

sorted(DataFrame['HP'])
q1,q3= np.percentile (DataFrame['HP'], [25,75]) #q1=84 #q3=140
iqr=q3-q1 #56

sorted(DataFrame['SP'])
q1,q3= np.percentile (DataFrame['SP'], [25,75])  #q1=113.8291 #q3=126.4043
iqr=q3-q1 #12.5751

sorted(DataFrame['VOL'])
q1,q3= np.percentile (DataFrame['VOL'], [25,75])  #q1=89 #q2=113
iqr=q3-q1 #24

sorted(DataFrame['WT'])
q1,q3= np.percentile (DataFrame['WT'], [25,75])  #q1=29.591 #q3=37.392
iqr=q3-q1 #7.80075


 # creating histograms on single graph
means = 117.469,98.765,121.54,32.412,34.422
stdevs = 56.7598,22.16340639,14.09362001,7.446417424,9.074902735

dist = pd.DataFrame(np.random.normal(loc=means, scale=stdevs, size=(81, 5)),
                    columns=['HP', 'VOL', 'SP', 'WT', 'MPG'])
dist.agg(['min', 'max', 'mean', 'std']).round(decimals=2)

fig, ax = plt.subplots()
dist.plot.kde(ax=ax, legend=False, title='Histogram of cloumns')
dist.plot.hist(density=True, ax=ax)
ax.grid(axis='y')
ax.set_facecolor('#d8dcd6')
plt.xlabel ('col')
plt.ylabel('distri')
plt.show()



     








































