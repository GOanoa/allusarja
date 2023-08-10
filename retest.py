import pandas as p
import matplotlib.pyplot as m
import seaborn as s
data=p.read_csv("mtcars.csv")
# HISTOGRAM
mpg=data['mpg']
m.hist(mpg,bins='auto',color='k',edgecolor='c')
m.xlabel('frequency')
m.ylabel('miles per gallon')
m.show()
# SCATTER
wt=data['wt']
iv=range(len(data))
m.scatter(iv,mpg,color='k')
m.scatter(iv,wt,color='g')
m.xlabel('weight')
m.ylabel('noof cars')
m.legend()
m.show()
# BAR PLOT
c=data['am'].value_counts()
co=['k','g']
m.bar(c.index,c.values,color=co,width=0.3)
m.xticks([0,1],['0-Automatic','1-Manual'])
m.show()
# BOX PLOT
s=data['am']
m.boxplot(mpg)
m.xlabel('frequency ')
m.ylabel('distribution of cars')
m.show()
