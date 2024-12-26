import pandas as pd
import numpy as np

df=pd.read_excel('Chase_melanie.xlsx')

dList=df['description'].tolist()
strippedList=[]

for desc in dList:
    new=''.join([c for c in desc if not c.isnumeric()])
    strippedList.append(new)

uniqueList=[]
[uniqueList.append(d) for d in strippedList if d not in uniqueList]

#print(uniqueList)

df['unique name']=strippedList
columns=df.columns.tolist()
dfSummary=pd.DataFrame({'description':uniqueList})

for name in uniqueList:
    costList=df.loc[df['unique name']==name,'amount'].tolist()
    dfSummary.loc[dfSummary['description']==name,'mean']=np.mean(costList)
    dfSummary.loc[dfSummary['description']==name,'median']=np.median(costList)
    dfSummary.loc[dfSummary['description']==name,'per month']=np.sum(costList)/11.75
    dfSummary.loc[dfSummary['description']==name,'total']=np.sum(costList)
    dfSummary.loc[dfSummary['description']==name,'count']=len(costList)
    if 'Type' in columns:
        Type=df.loc[df['unique name']==name,'Type'].tolist()[0]
        category=df.loc[df['unique name']==name,'Category'].tolist()[0]
        dfSummary.loc[dfSummary['description']==name,'Type']=Type
        dfSummary.loc[dfSummary['description']==name,'Category']=category
        
        


df.to_excel('updated chase_melanie.xlsx',index=False)
dfSummary.to_excel('chase_melanie summary.xlsx',index=False)
