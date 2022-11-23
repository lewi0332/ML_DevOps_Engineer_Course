import os
import sys
sys.path.append('/Users/derricklewis/Documents/Flatiron/udacity-MLDevOps-engineering-course/4_PROJECT_predict_customer_churn_with_clean_code/Project')
import pytest
from pathlib import Path
import logging
from churn_library import import_data, perform_eda, encoder_helper, perform_feature_engineering, train_models

logging.basicConfig(
    filename='./logs/churn_library.log',
    level = logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

@pytest.fixture()
def path():
	return ("./data/bank_data.csv", 'churn')

@pytest.fixture()
def dff(path):
	dff = import_data(path[0], path[1])
	return dff

@pytest.fixture()
def features(dff, path):
	x_train, x_test, y_train, y_test = perform_feature_engineering(dff, path[1])
	return (x_train, x_test, y_train, y_test)


def test_import(path):
	'''
	test data import - this example is completed for you to assist with the other test functions
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
		logging.error("Testing import_data: The file doesn't appear to have rows and columns")
		raise err


def test_eda(dff):
    '''
    test perform eda function
    '''
    # dff = import_data(path[0], path[1])
    perform_eda(dff)
    assert os.path.getsize('./images/churn.png') > 1
    assert os.path.getsize('./images/customer_age.png') > 1
    assert os.path.getsize('./images/marital_status.png') > 1
    assert os.path.getsize('./images/histplot.png') > 1
    assert os.path.getsize('./images/corr_plot.png') > 1


def test_encoder_helper(dff, path):
	'''
	test encoder helper 
	'''
	category_lst = dff.drop('CLIENTNUM', axis=1).select_dtypes(object).columns
	dff = encoder_helper(dff, category_lst, response=path[1])


def test_perform_feature_engineering(dff, path):
	'''
	test perform_feature_engineering
	'''
	perform_feature_engineering(dff, path[1])
	#assert columns are data type


def test_train_models(features):
	'''
	test train_models
	'''
	train_models(features[0], features[1], features[2], features[3])


# if __name__ == "__main__":
# 	pass







