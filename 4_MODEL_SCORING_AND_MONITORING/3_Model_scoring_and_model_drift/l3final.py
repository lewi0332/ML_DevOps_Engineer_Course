import pandas as pd
import pickle
from sklearn import metrics
from sklearn.metrics import f1_score
import ast
import numpy as np

with open('l3final.pkl', 'rb') as file:
    model = pickle.load(file)
  
testdata=pd.read_csv('testdatafinal.csv')

X = testdata['timeperiod'].values.reshape(-1,1)
y = testdata['sales'].values.reshape(-1,1)

predicted=model.predict(X)

print(predicted)

mse=metrics.mean_squared_error(predicted,y)

print(mse)

with open('l3finalscores.txt', 'r') as f:
    mselist = ast.literal_eval(f.read())

iqr = np.quantile(mselist,0.75)-np.quantile(mselist,0.25)

drifttest = mse>(np.quantile(mselist,0.75)+iqr*1.5)
print(drifttest)

