# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 19:36:40 2023

@author: jessa
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#reading excel
data = pd.read_excel('articles.xlsx')

#counting the number of articles per source

data.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher

data.groupby(['source_id'])['engagement_reaction_count'].sum()



data=data.drop('engagement_comment_plugin_count' , axis=1) 

#create a keyword
# keyword='murder'

# #for loop and flagging

# length = len(data)
# keyword_flag=[]
# for x in range(0,length):
#     heading=data['title'][x]
#     if keyword in heading:
#         flag=1
#     else:
#         flag=0
#     keyword_flag.append(flag)        


#make a function

def keyword_flag(keyword):
    length = len(data)
    keyword_flag=[]
    for x in range(0,length):
        heading=data['title'][x]
        try:
            if keyword in heading:
                flag=1
            else:
                flag=0
        except:
            flag=0
        keyword_flag.append(flag)        
    return keyword_flag

keyword_flag = keyword_flag('murder')

#creating a new column in data dataframe

data['KeyWord_Flag'] = pd.Series(keyword_flag)


#SentimentIntensityAnalyzer
title_neg_senti = []
title_pos_senti = []
title_neu_senti = []

length = len(data)
for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_senti.append(neg)
    title_pos_senti.append(pos)
    title_neu_senti.append(neu)

data['title_neg_sentiment'] = title_neg_senti
data['title_pos_sentiment'] = title_pos_senti
data['title_neu_sentiment'] = title_neu_senti

# write the data to excel

data.to_excel('blogme_cleaned.xlsx',sheet_name='blogmedata',index=False)














