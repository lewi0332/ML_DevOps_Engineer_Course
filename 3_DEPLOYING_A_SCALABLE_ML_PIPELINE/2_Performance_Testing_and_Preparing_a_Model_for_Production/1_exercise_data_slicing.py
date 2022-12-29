"""
1. Download the Iris data set from the UCI Machine Learning Repository
2. Load the data using Pandas and then write a function that outputs the descriptive stats for each numeric feature while the categorical variable is held fixed.
3. Run this function for each of the four numeric variables in the Iris data set.
"""


from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()

df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])


def slice_iris(df, target):
    num_cols = df.drop(target, axis=1).select_dtypes('number').columns
    for _ in df.target.unique():
        print(df[df.target == _][num_cols].describe())

slice_iris(df, 'target')




# def slice_iris(df, feature):
#     """ Function for calculating descriptive stats on slices of the Iris dataset."""
#     for cls in df["class"].unique():
#         df_temp = df[df["class"] == cls]
#         mean = df_temp[feature].mean()
#         stddev = df_temp[feature].std()
#         print(f"Class: {cls}")
#         print(f"{feature} mean: {mean:.4f}")
#         print(f"{feature} stddev: {stddev:.4f}")
#     print()


# slice_iris(df, "septal_length")
# slice_iris(df, "septal_width")
# slice_iris(df, "petal_length")
# slice_iris(df, "petal_width")