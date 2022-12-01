import os
import sys
from pandas.api.types import is_numeric_dtype
sys.path.append('/Users/derricklewis/Documents/Flatiron/udacity-MLDevOps-engineering-course/4_PROJECT_predict_customer_churn_with_clean_code/Project')
sys.path.append('/home/derricklewis/Documents/Data Science/udacity-MLDevOps-engineering-course/4_PROJECT_predict_customer_churn_with_clean_code/Project')
import pytest
from pathlib import Path
import logging
from churn_library import import_data, perform_eda, encoder_helper
from churn_library import perform_feature_engineering, train_models

logging.basicConfig(
    filename='./logs/churn_library.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


@pytest.fixture()
def path():
    '''
    Pytest fixture to store path
    '''
    return ("./data/bank_data.csv", 'churn')


@pytest.fixture()
def dff(path):
    '''
    Pytest fixture to pass dataframe to another test.
    '''
    dff = import_data(path[0], path[1])
    return dff


@pytest.fixture()
def features(dff, path):
    '''
    Pytest fixture to store features
    '''
    x_train, x_test, y_train, y_test = perform_feature_engineering(dff, path[1])
    return (x_train, x_test, y_train, y_test)


def test_import(request, path):
    '''
    test data import - this example is completed for you to 
    assist with the other test functions
    '''
    try:
        df = import_data(path[0], path[1])
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_eda: The file wasn't found")
        raise err
    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
    except AssertionError as err:
        logging.error("Testing import_data: The file doesn't appear to have \
            rows and columns")
        raise err


def test_eda(dff):
    '''
    test perform eda function
    '''
    logging.info("Starting EDA testing")
    perform_eda(dff)
    try:
        assert os.path.getsize('./images/eda/churn_distribution.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL: The churn_distribution image is missing %s", err)
        raise err
    except AssertionError as err:
        logging.error("FAIL: The churn_distribution image is empty %s", err)
        raise err
    try:
        assert os.path.getsize(
            './images/eda/customer_age_distribution.png') > 1
    except FileNotFoundError as err:
        logging.error(
            "FAIL: The customer age distribution image is missing %s", err)
        raise err
    except AssertionError as err:
        logging.error(
            "FAIL: The customer age distribution image is empty %s", err)
        raise err
    try:
        assert os.path.getsize(
            './images/eda/marital_status_distribution.png') > 1
    except FileNotFoundError as err:
        logging.error(
            "FAIL: The marital status distribution image is missing %s", err)
        raise err
    except AssertionError as err:
        logging.error(
            "FAIL: The marital status distribution image is empty %s", err)
        raise err
    try:
        assert os.path.getsize(
            './images/eda/total_transaction_distribution.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL: The Total Transactions distribution image is \
            missing %s", err)
        raise err
    except AssertionError as err:
        logging.error(
            "FAIL: The Total Transactions distribution image is empty %s", err)
        raise err
    try:
        assert os.path.getsize('./images/eda/heatmap.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL: The heatmap image is missing %s", err)
        raise err
    except AssertionError as err:
        logging.error("FAIL: The heatmap image is empty %s", err)
        raise err


def test_encoder_helper(dff, path):
    '''
    test encoder helper
    '''
    logging.info("Starting encoder_helper test")
    logging.info("Building list of categorical variables")
    category_lst = dff.select_dtypes(object).columns
    init_col_cnt = len(dff.columns)
    try:
        assert len(category_lst) > 0
        logging.info("Categorical List has at least 1 column")
    except AssertionError as err:
        logging.error("FAIL: The category list %s", err)
        raise err
    try:
        logging.info("Starting to encode columns")
        dff_enc = encoder_helper(dff, category_lst, response=path[1])
        logging.info("SUCCESS: Encoder function ran.")
    except Exception as err:
        logging.error("An error occur testing the Encode Function: %s", err)
        raise err
    try:
        assert len(dff_enc.columns) > init_col_cnt
    except AssertionError as err:
        logging.error("FAIL: Encoded DF has no new columns")
        raise err
    try:
        for category in category_lst:
            assert dff[f'{category}_Churn'].dtypes == float
    except AssertionError as err:
        logging.error("Encoded categories not floats: %s", err)
        raise err


def test_perform_feature_engineering(dff, path):
    '''
    test perform_feature_engineering
    '''
    x_train, x_test, y_train, y_test = perform_feature_engineering(dff, path[1])
    #assert columns are data type
    try:
        for feature in dff.columns:
            assert is_numeric_dtype(x_train[feature])
    except AssertionError as err:
        logging.error("Encoded categories not floats: %s", err)
        raise err


def test_train_models(features):
    '''
    test train_models
    '''
    train_models(features[0], features[1], features[2], features[3])
    try:
        assert os.path.getsize('./images/results/feature_importances.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL: The feature_importances image is missing %s", err)
        raise err
    except AssertionError as err:
        logging.error("FAIL: The feature_importances image is empty %s", err)
        raise err
    try:
        assert os.path.getsize(
            './images/results/classification_report_Random_Forest.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL: The rf_results.png image is missing %s", err)
        raise err
    except AssertionError as err:
        logging.error("FAIL: The rf_results.png image is empty %s", err)
        raise err
    try:
        assert os.path.getsize(
            './images/results/classification_report_Logistic_Regression.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL: The logistic_results.png image is missing %s", err)
        raise err
    try:
        assert os.path.getsize('./images/results/roc_curve_result.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL: The roc_curve_result image is missing %s", err)
        raise err
    except AssertionError as err:
        logging.error("FAIL: The roc_curve_result image is empty %s", err)
        raise err
    try:
        assert os.path.getsize('./models/logistic_model.pkl') > 1
    except FileNotFoundError as err:
        logging.error("FAIL: logistic_model is missing %s", err)
        raise err
    except AssertionError as err:
        logging.error("FAIL: logistic_model is empty %s", err)
        raise err
    try:
        assert os.path.getsize('./models/rfc_model.pkl') > 1
    except FileNotFoundError as err:
        logging.error("FAIL: rfc_model is missing %s", err)
        raise err
    except AssertionError as err:
        logging.error("FAIL: rfc_model is empty %s", err)
        raise err