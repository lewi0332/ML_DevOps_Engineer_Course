import ast
import pandas as pd
import numpy as np

recent_r2=0.6
recent_sse=52938


#record a score in a DataFrame
previousscores=pd.read_csv('previousscores.csv')


#find the maximum version number
maxversion=previousscores['version'].max()

thisversion=maxversion+1


new_row_r2 = {'metric':'r2', 'version':thisversion, 'score':recent_r2}
new_row_sse = {'metric':'sse', 'version':thisversion, 'score':recent_sse}

if recent_sse<previousscores.loc[previousscores['metric']=='sse','score'].min():
    previousscores = previousscores.append(new_row_r2, ignore_index=True)
    previousscores = previousscores.append(new_row_sse, ignore_index=True)
    previousscores.to_csv('newscores.csv')






