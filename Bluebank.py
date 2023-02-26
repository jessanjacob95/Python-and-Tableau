# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:15:38 2023

@author: jessa
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

#Loading up json file

json_file=open('loan_data_json.json')
data=json.load(json_file)

#Data to Dataframe

loandata=pd.DataFrame(data)

#add annualincome to

loandata['Annual_Income'] = np.exp(loandata['log.annual.inc'])

fico = 700

#fico >= 300 and < 400:'Very Poor'
#fico >= 400 and ficoscore < 600:'Poor'
#fico >= 601 and ficoscore < 660:'Fair'
#fico >= 660 and ficoscore < 780:'Good'
#fico >=780:'Excellent'

length = len(loandata)
ficocat = []
for x in range(0,length):
   
    category = loandata['fico'][x]

    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >=700:
        cat = 'Excellent'
    else:
        cat = 'Unknown'    
    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loandata['fico_category'] = ficocat


loandata.loc[loandata['int.rate'] >0.12 , 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <=0.12 , 'int.rate.type'] = 'Low'

#Number of loans per category

catplot = loandata.groupby(['fico_category']).size()
catplot.plot.bar(color = 'green' , width = 0.2)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='orange' , width = 0.2)
plt.show()

#Scatter plot

ypoint = loandata['Annual_Income']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint, color = 'lightgreen')
plt.show()

#export as csv
loandata.to_csv('loandata_cleaned.csv' , index = True)






















