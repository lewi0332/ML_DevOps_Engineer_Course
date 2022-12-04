"""
Module with functions for Churn model

Author: Udacity
Date: November 2022
"""

# import libraries
import logging
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import RocCurveDisplay, classification_report
import pandas as pd
import shap
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

os.environ['QT_QPA_PLATFORM'] = 'offscreen'

logging.basicConfig(
    filename="./logs/churn_library.log",
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


def import_data(pth, response='churn'):
    '''
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
    '''
    try:
        logging.info("Opening %s", pth)
        # drop index if present ignore otherwise
        dff = pd.read_csv(pth).drop('Unnamed: 0', axis=1, errors='ignore')
        logging.info('SUCCESS: Read in %d rows of data', len(dff))
    except FileNotFoundError as err:
        logging.error(err)
        raise err
    try:
        logging.info("Creating target varible with name: %s", response)
        dff[response] = dff['Attrition_Flag'].apply(
            lambda val: 0 if val == "Existing Customer" else 1)
        dff.drop('Attrition_Flag', axis=1, inplace=True)
        logging.info("SUCCESS: created target variable.")
    except KeyError as err:
        logging.error("FAIL: %(target)s not a column in DF. %(error)s",
                      {'target': response, 'error': err})
        raise err
    except Exception as err:
        logging.error("FAIL: Could not create column: %s", err)
        raise err
    try:
        logging.info('Attempting to remove CLIENTNUM from dataframe.')
        dff.drop('CLIENTNUM', axis=1, inplace=True)
        logging.info('SUCESS: Removed CLIENTNUM from df')
    except KeyError as err:
        logging.error("FAIL: %(target)s not a column in DF. %(error)s",
                      {'target': 'CLIENTNUM', 'error': err})
        raise err
    return dff


def perform_eda(dff):
    '''
    perform eda on df and save figures to images folder
    input:
            df: pandas dataframe

    output:
            None
    '''
    # print(dff.head)
    # print(dff.shape)
    # print(dff.isnull().sum())

    try:
        logging.info("Attempting churn view.")
        plt.figure(figsize=(20, 10))
        dff['churn'].hist()
        plt.savefig('./images/eda/churn_distribution.png')
    except KeyError as err:
        logging.error("FAIL: The Churn column is missing from the dataFrame.\
                Could not visualize. (%s)", err)
        raise err
    try:
        logging.info("Attempting Customer_age view.")
        plt.figure(figsize=(20, 10))
        dff['Customer_Age'].hist()
        plt.savefig('./images/eda/customer_age_distribution.png')
    except KeyError as err:
        logging.error("FAIL: The Customer_Age column is missing from the \
                dataFrame. Could not visualize. (%s)", err)
        raise err
    try:
        logging.info("Attempting Marital_Status view.")
        plt.figure(figsize=(20, 10))
        dff.Marital_Status.value_counts('normalize').plot(kind='bar')
        plt.savefig('./images/eda/marital_status_distribution.png')
    except KeyError as err:
        logging.error("FAIL: The Marital_Status column is missing from the \
                dataFrame. Could not visualize. (%s)", err)
        raise err

    try:
        logging.info("Attempting Total_Trans_Ct view.")
        plt.figure(figsize=(20, 10))
        sns.histplot(dff['Total_Trans_Ct'], stat='density', kde=True)
        plt.savefig('./images/eda/total_transaction_distribution.png')
    except KeyError as err:
        logging.error("FAIL: The Total_Trans_Ct column is missing from the \
                dataFrame. Could not visualize. (%s)", err)
        raise err

    try:
        logging.info("Attempting correlation heat map view.")
        plt.figure(figsize=(20, 10))
        sns.heatmap(dff.corr(),
                    annot=False,
                    cmap='Dark2_r',
                    linewidths=2)
        plt.savefig('./images/eda/heatmap.png')
    except TypeError as err:
        logging.error("FAIL: The correlation of the DF failed due to \
            TypeError: %s", err)
    except FileNotFoundError as err:
        logging.error("FAIL: The correlation heatmap failed. \
                Could not visualize. More info here: %s", err)
    except Exception as err:  # Not sure why this could fail, leaving it open
        logging.error("FAIL: The correlation heatmap failed. \
                Could not visualize. More info here: %s", err)
        raise err


def encoder_helper(dff, category_lst, response='churn'):
    '''
    helper function to turn each categorical column into a new column with
    propotion of churn for each category - associated with cell 15 from the
    notebook

    input:
            df: pandas dataframe
            category_lst: list of columns that contain categorical features
            response: string of response name [optional argument that could be
            used for naming variables or index y column]

    output:
            df: pandas dataframe with new columns for
    '''

    for category in category_lst:
        try:
            logging.info("Creating encoded column %s", category)
            temp_cat_lst = []
            groups = dff.groupby(category).mean()[response]

            for val in dff[category]:
                temp_cat_lst.append(groups.loc[val])

            dff[f'{category}_Churn'] = temp_cat_lst
            logging.info("SUCCESS: created encoded %s column.", category)
        except KeyError as err:
            logging.error("FAIL: %s is not a column in the DataFrame. \
                    %(error)s", {"col": category, "error": err})
            raise err
        except Exception as err:
            logging.error("FAIL: Could not create column. %s", err)
            raise err
    return dff


def perform_feature_engineering(dff, response='churn'):
    '''
    input:
              df: pandas dataframe
              response: string of response name [optional argument that could
              be used for naming variables or index y column]

    output:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    '''
    category_lst = dff.select_dtypes(object).columns

    dff = encoder_helper(dff, category_lst, response=response)

    try:
        logging.info("Splitting DataFrame into Features and Target...")
        target = dff.pop(response)
        features = dff.select_dtypes(include=np.number)
        logging.info('SUCCESS: Split dataframe into %d "X" features and "y" \
target created.', len(features.columns))
        logging.info("Splitting data into Train and Test sets")
        x_train, x_test, y_train, y_test = train_test_split(features,
                                                            target,
                                                            test_size=0.3,
                                                            random_state=42)
        logging.info("SUCCESS: Data sets split into %(train_len)d training \
rows and %(test_len)d test rows.",
                     {"train_len": len(x_train), "test_len": len(x_test)})
    except Exception as err:
        logging.error("FAIL: Could not split dataset: %s", err)
        raise err
    return x_train, x_test, y_train, y_test


def classification_report_image(y_train,
                                y_test,
                                y_train_preds,
                                y_test_preds,
                                model_type,
                                output_pth):
    '''
    produces classification report for training and testing results and stores
    report as image in images folder
    input:
            y_train: training response values
            y_test:  test response values
            y_train_preds: training predictions from logistic regression
            y_test_preds: test predictions
            model_type: String naming model type
            output_pth: path to store images of the classification report

    output:
             None
    '''
    try:
        logging.info('Starting classification report for %s', model_type)
        plt.figure(figsize=(5, 5))
        # plt.rc("figure", figsize=(5, 5))
        plt.text(0.01, 1.25, str(model_type + " Test"),
                 {'fontsize': 10},
                 fontproperties='monospace')
        plt.text(0.01, 0.05, str(classification_report(y_test, y_test_preds)),
                 {'fontsize': 10}, fontproperties='monospace')
        plt.text(0.01, 0.6, str(model_type + " Train"), {'fontsize': 10},
                 fontproperties='monospace')
        plt.text(0.01, 0.7, str(classification_report(y_train, y_train_preds)),
                 {'fontsize': 10}, fontproperties='monospace')
        plt.axis('off')
        plt.savefig(output_pth + 'classification_report_' + model_type +
                    '.png')
        logging.info("SUCCESS: Plot for type %(model)s saved to %(path)s",
                     {'model': model_type, 'path': output_pth})
    except Exception as err:
        logging.error('FAIL: could not save classification report %(model)s \
            to %(path)s because of %(exc)s',
                      {'model': model_type, 'path': output_pth, 'exc': err})
        raise err


def feature_importance_plot(model, x_data, output_pth):
    '''
    creates and stores the feature importances in pth
    input:
            model: model object containing feature_importances_
            X_data: pandas dataframe of X values
            output_pth: path to store the figure

    output:
             None
    '''
    try:
        logging.info("Starting importance plot")
        # Calculate feature importances
        importances = model.best_estimator_.feature_importances_
        logging.info("SUCCESS: collected %d important features from model\
            for feature importance plot",
                     len(importances))
        # Sort feature importances in descending order
        indices = np.argsort(importances)[::-1]
        logging.info("SUCCESS: Gather indices of features important features")
        # Rearrange feature names so they match the sorted feature importances
        names = [x_data.columns[i] for i in indices]
        logging.info("SUCCCSS: Gathered %d feature names to label plot.",
                     len(names))
        # Create plot
        plt.figure(figsize=(20, 5))

        # Create plot title
        plt.title("Feature Importance")
        plt.ylabel('Importance')

        # Add bars
        plt.bar(range(x_data.shape[1]), importances[indices])

        # Add feature names as x-axis labels
        plt.xticks(range(x_data.shape[1]), names, rotation=90)
        plt.savefig(output_pth)
        logging.info("SUCCESS: Plot stored at %s", output_pth)
    except Exception as err:
        logging.error("FAIL: plot most important features: %s", err)


def train_models(x_train, x_test, y_train, y_test):
    '''
    train, store model results: images + scores, and store models
    input:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    output:
              None
    '''
    # grid search
    rfc = RandomForestClassifier(random_state=42)
    # Use a different solver if the default 'lbfgs' fails to converge
    # Reference:
    # https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
    lrc = LogisticRegression(solver='lbfgs', max_iter=3000)

    param_grid = {
        'n_estimators': [200, 500],
        # `max_features='auto'` has been deprecated in 1.1
        # 'max_features': ['auto', 'sqrt'],
        'max_depth': [4, 5, 100],
        'criterion': ['gini', 'entropy']
    }

    cv_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5)
    cv_rfc.fit(x_train, y_train)

    lrc.fit(x_train, y_train)

    y_train_preds_rf = cv_rfc.best_estimator_.predict(x_train)
    y_test_preds_rf = cv_rfc.best_estimator_.predict(x_test)

    y_train_preds_lr = lrc.predict(x_train)
    y_test_preds_lr = lrc.predict(x_test)

    try:
        # scores
        classification_report_image(y_train,
                                    y_test,
                                    y_train_preds_rf,
                                    y_test_preds_rf,
                                    'Random_Forest',
                                    './images/results/')

        classification_report_image(y_train,
                                    y_test,
                                    y_train_preds_lr,
                                    y_test_preds_lr,
                                    'Logistic_Regression',
                                    './images/results/')
    except Exception as err:
        logging.error("FAIL: could not plot classification report: %s", err)
    try:
        # plots
        plt.figure(figsize=(15, 8))
        axis = plt.gca()
        RocCurveDisplay.from_estimator(lrc,
                                       x_test,
                                       y_test,
                                       ax=axis,
                                       alpha=0.8)
        RocCurveDisplay.from_estimator(cv_rfc,
                                       x_test,
                                       y_test,
                                       ax=axis,
                                       alpha=0.8)
        plt.savefig('./images/results/roc_curve_result.png')
    except Exception as err:
        logging.error("FAIL: could not plot Roc Auc report: %s", err)
    try:
        # save best models
        joblib.dump(cv_rfc.best_estimator_, './models/rfc_model.pkl')
        joblib.dump(lrc, './models/logistic_model.pkl')
    except Exception as err:
        logging.error("Could not store model.pkl files: %s", err)
        raise err
    try:
        explainer = shap.TreeExplainer(cv_rfc.best_estimator_)
        shap_values = explainer.shap_values(x_test)

        plt.figure(figsize=(15, 8))
        axis = plt.gca()
        shap.summary_plot(shap_values, x_test, plot_type="bar", show=False)
        plt.savefig('./images/results/shap_values.png')
    except Exception as err:
        logging.error("Could not plot shap values: %s", err)
    try:
        feature_importance_plot(cv_rfc,
                                x_train,
                                './images/results/feature_importances.png')
    except Exception as err:
        logging.error("Could not plot feature importance: %s", err)


def main(data_path, response):
    """
    Main function to train model.
    Input
    ---
    data_path: str, the path to the csv data file
    response: str, the name the classification target should be given

    Output
    ---
    "Complete" will be printed to the console after successfully
    saving visuals and serialized models to the directory.
    """
    dff = import_data(data_path, response)
    perform_eda(dff)
    x_train, x_test, y_train, y_test = perform_feature_engineering(dff,
                                                                   response)
    train_models(x_train, x_test, y_train, y_test)
    return print("Complete")


if __name__ == "__main__":
    main(r"./data/bank_data.csv", 'churn')
