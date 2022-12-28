from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()

df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])


def slice_iris(df, target):
    num_cols = df.drop(target, axis=1).select_dtypes('number').columns
    for _ in df.target.unique():
        print(df[df.target == _][num_cols].describe())


slice_iris(df, 'target')