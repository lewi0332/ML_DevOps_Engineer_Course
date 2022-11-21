## STEPS TO COMPLETE ##
# 1. import logging
# 2. set up config file for logging called `results.log`
# 3. add try except with logging for success or error
#    in relation to checking the types of a and b
# 4. check to see that log is created and populated correctly
#    should have error for first function and success for
#    the second
# 5. use pylint and autopep8 to make changes
#    and receive 10/10 pep8 score
"""
This module sums two integers

Auther: Derrick
Date: November 19th
"""
import logging

logging.basicConfig(
    filename="./results.log",
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'
)

def sum_vals(first_int, second_int):
    '''
    Args:
        first_int: (int)
        second_int: (int)
    Return:
        first_int + second_int (int)
    '''
    try:
        logging.info(f"{first_int}, {second_int}")
        assert isinstance(first_int, int)
        assert isinstance(second_int, int)
        logging.info("SUCCESS: both parameters integer data type")
        return first_int+second_int
    except AssertionError:
        logging.error("FAIL: Input not an integer.")
        return None

if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(4, 5)
