import numpy as np
import pandas as pd
file=open('YahooMovies.txt','r',encoding='utf-8-sig')
strlist=file.readlines()
allrows=list()
for eachrow in strlist:
    eachrowlist=eachrow.split()
    wordslist=eachrowlist[:2]
    wordslist+=[' '.join(eachrowlist[2:-1])]
    wordslist+=[eachrowlist[-1][1:-1]]
    allrows.append(wordslist)
np1=np.array(allrows)
pd_data = pd.DataFrame(np1,columns=['Score','Viewing','Title','Year'])
pd_data.to_csv('YM.csv')