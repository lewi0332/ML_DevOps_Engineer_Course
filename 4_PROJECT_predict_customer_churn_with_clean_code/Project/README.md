# Predict Customer Churn

- Project **Predict Customer Churn** of ML DevOps Engineer Nanodegree Udacity

---

This project trains a model to identify credit card customers that are most likely to churn. 

## Project Description
The project uses a labeld data file with information on credit card customers and trains two classification models to predict the likelihood of a customer. Exploratory Data Analysis is first performed on the data to view the distrobution of key characteristics and correlations. The data is then prepared with categorical encodings and feature engineering before 2 models are trained: Random Forest Classifier and Logistic Regression. Results of each model's performance are stored and as well as a serialized file of the model to be used for future preditions. 

The project contains a test script to be used to ensure each function works as intended and logs are stored for each. 

This project is part of a Udacity Nanodegree program for ML DevOps Engineering and is test to create clean code principles. Functions and model training design has been written by Udacity. The script sctucture, logging, and test script have been updated by Derrick Lewis. 

## Files and data description
Overview of the files and data present in the root directory. 

### Data
- `./data/bank_data.csv`: Demographics and credit account data on bank consumers. Including a target classification column labeled `Attrition_flag` with a value of *Attrited Customer* or *Existing Customer* designating the classification to predict

### Files
- [churn_notebook.ipynb](churn_notebook.ipynb): This file includes the original development of the functions, Exploratory Data Analysis and training. It was used to formulate the test various techniques and is not needed to run this final project. 
- [churn_library.py](churn_library.py): This is the primary file to train the model and create visualiztions. It uses two algorithms from Scikit-Learn: Random Forrest and Logistic Regression. 
- [churn_script_logging_and_tests.py](churn_script_logging_and_tests.py): This is the primary file for testing and validating the script and it's functions are working as intended. 
- [/images](./images/): Directory containing images
  - [/images/eda](./images/eda/): Distribution and data analysis for churn classification, age, marital status, transactions, and a heatmap of correlation of features.
  - [/images/results](./images/results/): Receiver operating characteristic curve, classification reports for bot logistic regression and random forrest models and a Shapley values feature importance visual. 
- [/logs](/logs/): Directory containing log files of either training or testing of the project. 
- [/models](/models/): Serialized models after training. 
- [/data](/data/): directory to store data file to be used in model training.

## Running Files


#### Installation

1. Install necessary libraries using pip
    - `conda env create -f environment.yml`

2. Activate the Envirnoment
    - `conda activate churn`

### Running main file:
After installing and activating the conda env above, you can run the primary training file with the command below in the command line.

```
python churn_library.py
```

Necessary data and folder structure above should be in place before running this. 

The script will load data from the `.csv` in `/data/` directory, transform categorical variables 

### Running test file:

```
pytest churn_script_logging_and_tests.py
```

## Author

-   **Derrick Lewis**  [Portfolio Site](https://www.derrickjameslewis.com) - [linkedin](https://www.linkedin.com/in/derrickjlewis/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

I would like to thank [Udacity](https://eu.udacity.com/) for this amazing project
