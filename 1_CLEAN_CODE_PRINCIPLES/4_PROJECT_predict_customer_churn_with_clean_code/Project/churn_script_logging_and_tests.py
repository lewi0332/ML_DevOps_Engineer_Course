""""
Module to test churn script functions using Pytest.

Author: Derrick
Date: November 2022
"""

import os
import logging
import pytest
from pandas.api.types import is_numeric_dtype
from Project.churn_library import import_data, perform_eda, encoder_helper
from Project.churn_library import perform_feature_engineering, train_models

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
    Pytest fixture to pass dataframe to various tests.
    '''
    dff_ = import_data(path[0], path[1])
    return dff_


@pytest.fixture()
def features(dff, path):
    '''
    Pytest fixture to cache feature engineered dataset splits before training.
    '''
    x_train, x_test, y_train, y_test = perform_feature_engineering(
        dff, path[1])
    return (x_train, x_test, y_train, y_test)


def test_import(path):
    '''
    test data import - This tests the ability to load the training data.
    '''
    try:
        dff_ = import_data(path[0], path[1])
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_data(): The file wasn't found: %s", err)
    try:
        assert dff_.shape[0] > 0
        assert dff_.shape[1] > 0
    except AssertionError as err:
        logging.error("Testing import_data(): The file was loaded but,\
         doesn't appear to have rows and columns: %s", err)


def test_eda(dff):
    '''
    test perform eda function
    '''
    logging.info("Starting EDA testing")
    perform_eda(dff)
    try:
        assert os.path.getsize('./images/eda/churn_distribution.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL perform_eda(): The churn_distribution \
            image is missing %s", err)
    except AssertionError as err:
        logging.error("FAIL perform_eda(): The churn_distribution \
            image is empty %s", err)
    try:
        assert os.path.getsize(
            './images/eda/customer_age_distribution.png') > 1
    except FileNotFoundError as err:
        logging.error(
            "FAIL perform_eda(): The customer age distribution \
                image is missing %s", err)
    except AssertionError as err:
        logging.error(
            "FAIL perform_eda(): The customer age distribution \
                image is empty %s", err)
    try:
        assert os.path.getsize(
            './images/eda/marital_status_distribution.png') > 1
    except FileNotFoundError as err:
        logging.error(
            "FAIL perform_eda(): The marital status distribution \
                image is missing %s", err)
    except AssertionError as err:
        logging.error(
            "FAIL perform_eda(): The marital status distribution \
                image is empty %s", err)
    try:
        assert os.path.getsize(
            './images/eda/total_transaction_distribution.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL perform_eda(): The Total Transactions \
            distribution image is missing %s", err)
    except AssertionError as err:
        logging.error(
            "FAIL perform_eda(): The Total Transactions distribution \
                image is empty %s", err)
    try:
        assert os.path.getsize('./images/eda/heatmap.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL perform_eda(): The heatmap image is \
            missing %s", err)
    except AssertionError as err:
        logging.error("FAIL perform_eda(): The heatmap image is empty %s", err)


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
    try:
        logging.info("Starting to encode columns")
        dff_enc = encoder_helper(dff, category_lst, response=path[1])
        logging.info("SUCCESS: Encoder function ran.")
        assert len(dff_enc.columns) > init_col_cnt
    except AssertionError as err:
        logging.error("FAIL encoder_helper(): Encoded DF has no \
            new columns: %s", err)
    try:
        for category in category_lst:
            assert dff[f'{category}_Churn'].dtypes == float
    except AssertionError as err:
        logging.error("FAIL encoder_helper(): Encoded categories \
            not floats: %s", err)


def test_perform_feature_engineering(dff, path):
    '''
    test perform_feature_engineering
    '''
    x_train, x_test, y_train, y_test = perform_feature_engineering(
        dff, path[1])
    try:
        for feature in x_train.columns:
            assert is_numeric_dtype(x_train[feature])
    except AssertionError as err:
        logging.error("FAIL perform_feature_engineering(): x_train \
            not numeric: %s", err)
    try:
        for feature in x_test.columns:
            assert is_numeric_dtype(x_test[feature])
    except AssertionError as err:
        logging.error("FAIL perform_feature_engineering(): x_test not \
            numeric: %s", err)
    try:
        assert is_numeric_dtype(y_train)
    except AssertionError as err:
        logging.error("FAIL perform_feature_engineering(): y_train not \
            numeric: %s", err)
    try:
        assert is_numeric_dtype(y_test)
    except AssertionError as err:
        logging.error("FAIL perform_feature_engineering(): y_test not \
            numeric: %s", err)


def test_train_models(features):
    '''
    test train_models
    '''
    train_models(features[0], features[1], features[2], features[3])
    try:
        assert os.path.getsize('./images/results/feature_importances.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL train_models(): The feature_importances \
            image is missing %s", err)
    except AssertionError as err:
        logging.error("FAIL train_models(): The feature_importances \
            image is empty %s", err)
    try:
        assert os.path.getsize(
            './images/results/classification_report_Random_Forest.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL train_models(): The rf_results.png image is \
            missing %s", err)
    except AssertionError as err:
        logging.error("FAIL train_models(): The rf_results.png image is \
            empty %s", err)
    try:
        assert os.path.getsize(
            './images/results/classification_report_Logistic_Regression.png'
            ) > 1
    except FileNotFoundError as err:
        logging.error(
            "FAIL: The logistic_results.png image is missing %s", err)
    try:
        assert os.path.getsize('./images/results/roc_curve_result.png') > 1
    except FileNotFoundError as err:
        logging.error("FAIL train_models(): The roc_curve_result \
            image is missing %s", err)
    except AssertionError as err:
        logging.error("FAIL train_models(): The roc_curve_result \
            image is empty %s", err)
    try:
        assert os.path.getsize('./models/logistic_model.pkl') > 1
    except FileNotFoundError as err:
        logging.error("FAIL train_models(): logistic_model is missing %s", err)
    except AssertionError as err:
        logging.error("FAIL train_models(): logistic_model is empty %s", err)
    try:
        assert os.path.getsize('./models/rfc_model.pkl') > 1
    except FileNotFoundError as err:
        logging.error("FAIL train_models(): rfc_model is missing %s", err)
    except AssertionError as err:
        logging.error("FAIL train_models(): rfc_model is empty %s", err)
