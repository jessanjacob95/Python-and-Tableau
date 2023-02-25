# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 07:00:17 2023

@author: jessa
"""

import pandas as pd

#filename = pd.read_csv(filename.csv)

data=pd.read_csv('transaction.csv')

data=pd.read_csv('transaction.csv', sep=';')

#Summary of the data

data.info()

# working with calculations

# defining variables

Cost_per_Item = 11.73
Selling_Price_per_Item = 21.11
Number_of_Items_Purchased = 6

#Mathematical operations on Tableau

Profit_per_Item = Selling_Price_per_Item - Cost_per_Item

Profit_per_Transaction = Profit_per_Item * Number_of_Items_Purchased
Cost_per_Transaction = Cost_per_Item * Number_of_Items_Purchased
Selling_Price_per_Transaction = Selling_Price_per_Item * Number_of_Items_Purchased


data['CostperTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SellingpriceperTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitperTransaction'] = data['SellingpriceperTransaction'] - data['CostperTransaction']
data['Markup'] = (data['SellingpriceperTransaction'] - data['CostperTransaction'])/data['CostperTransaction']

data['Markup'] = round(data['Markup'],2)

#Create date

day = data['Day'].astype(str)
year = data['Year'].astype(str)

data['Date'] = day+'-'+data['Month']+'-'+year


#Split the column and seperate the components

Split_Col = data['ClientKeywords'].str.split(',', expand=True)

#Name and put the columns inside the data

data['ClientAge'] = Split_Col[0]
data['ClientType'] = Split_Col[1]
data['LengthofContract'] = Split_Col[2]


#Remove the brackets

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')


# Change to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#How to merge files
#Bringing a new dataset

seasons=pd.read_csv('value_inc_seasons.csv', sep=';')

#merge the files

data=pd.merge(data,seasons,on='Month')

#Drop recurring coloumns

data=data.drop(['Day','Month','Year','ClientKeywords'],axis=1)

#Export as csv

data.to_csv('ValueInc_Cleaned.csv',index=False)












































