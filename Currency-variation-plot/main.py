import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np
link="http://api.fixer.io/"
res=requests.get(link+"latest",params={'base':'INR'})
curr=['USD','EUR','JPY','BRL','CAD','CHF','MXN','ILS','GBP']
dict={}
dict['Date']=[res.json()['date']]
for i in curr:
    dict[i]=[1/(res.json()['rates'][i])]
marr=[0,31,28,31,30,31,30,31,31,30,31,30,31]
date=res.json()['date']
day=int(date[8:])
month=int(date[5:7])
year=int(date[:4])
for i in range(6):
    if(day>1):
        day=day-1
    elif(month>1):
        month=month-1
        day=marr[month]
    else:
        day=31
        month=12
        year=year-1
    sd=str(day)
    sm=str(month)
    sy=str(year)
    if(day<10):
        sd="0"+sd
    if(month<10):
        sm="0"+sm
    dstr=sy+"-"+sm+"-"+sd
    res=requests.get(link+dstr,params={'base':'INR'})
    date=res.json()['date']
    day=int(date[8:])
    month=int(date[5:7])
    year=int(date[:4])
    dict['Date'].append(res.json()['date'])
    for j in curr:
        dict[j].append(1/(res.json()['rates'][j]))
df=pd.DataFrame(dict)
df.plot()
plt.xticks(np.array([0,1,2,3,4,5,6]),df['Date'])
plt.ylabel('Currency value [in INR]')
plt.xlabel('Date')
plt.title('Currency values for last 7 days')
plt.show()
