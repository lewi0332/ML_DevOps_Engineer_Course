# Data Exploration and Preperation

**Exploratory Data Analysis (EDA)**

The Exploratory Data Analysis is one of the first steps we typically execute in a project, before we jump into developing the ML pipeline. It is important to:

 - Maximize our understanding of the data (types, ranges, cardinality, correlations, outliers...)
 - Identify and correct data problems
 - Test our assumptions about the problem
 - Uncover data biases that can result in a biased model (for example, an unfair model with respect to some protected category)

For a good EDA you need intuition and creativity, so it is not possible to define a complete recipe. However, some things to look at are:

 - Understand what each feature means
 - Univariate analysis to verify that our expectation on that feature matches reality
 - Bivariate analysis where we look for correlations
 - Anomaly detection
 - Missing values handling


### Execute and Track an EDA in Jupyter

Even though the EDA is an interactive step, we want to make it reproducible and to track it. A simple strategy to accomplish this is:

1. Write an MLflow component that installs Jupyter and all the libraries that we need, and execute the EDA as a notebook from within this component
2. Embed plots and comments into the Jupyter notebook itself
3. Track inputs and outputs of the notebook with your artifact tracking, in our case Weights & Biases

Tracking a notebook in W&B is as simple as adding the `save_code=True` option when creating the run:

```
run = wandb.init(
  project="my_exercise",
  save_code=True
)
```
Demo: Pandas-Profiling

[Pandas-profiling](https://github.com/ydataai/pandas-profiling) is a tool to help with the EDA. A profile is an interactive visualization of the main characteristics of the dataset. It can be generated with:

```
# conda install -c conda-forge pandas-profiling
import pandas_profiling
import pandas as pd

df = pd.read_parquet("data.parquet") # or pd.read_csv()
profile = pandas_profiling.ProfileReport(df)
profile.to_widgets()
profile.to_file("your_report.html")
```

## Clean and Pre-process the Data

The pre-processing step is right at the beginning of the ML pipeline, just after data fetching. It implements the cleaning steps and other pre-processing that we have learned during the EDA.

It is however important to note that if an operation is needed for the training and validation data as well as for the production data, it **should not** be part of the pre-processing step. It should instead go in the inference pipeline, as we shall see in another video.

In other words, the pre-processing step should only apply transformations that are needed to make the training and test data look like what the model will encounter in production.
