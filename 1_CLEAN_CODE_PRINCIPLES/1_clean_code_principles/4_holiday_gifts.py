"""
Module to get the total cost of offer to give free gift to all users with wishlists.
(Testing Pylint and AutoPep8)

Author: Derrick
Date: November 2022
"""

import numpy as np


def get_total_gift_cost(wishlist_pth: str, max_price:int=25, tax:float=1.08) -> int:
    """
    Calculates the total cost to offer everyone a free gift under $25

    Args
    ---
    - wishliest_pth: (str) The path to the data of all wishlists
    - max_price: (int) The maximum price for a gift to qualify as free. Default is $25
    - tax: (float) The tax that will be added to the price of the gift when
    calculating the total price for the offer. Default is 1.08.

    Returns
    ---
    - The total price of offering all wishlists a free gift.

    """
    #open path
    with open(wishlist_pth,  encoding="utf-8") as file:
        gift_costs = file.read().split('\n')
    #Convert to numpy array of integers
    gift_costs = np.array(gift_costs).astype(int)
    #Calculate total cost 
    return (gift_costs[gift_costs<max_price] *tax).sum()

if __name__ == "__main__":
    TOTAL_PRICE = get_total_gift_cost('gift_costs.txt' )
    print(f"This offer would cost {TOTAL_PRICE} in total.")
