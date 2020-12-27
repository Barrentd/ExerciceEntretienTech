
"""Function that return the sum of price with a discount"""

import math

def calculate_total_price(prices, discount):

    """Calculate the price with a discount and return the sum
    Returns:
        int: sum of discount price
    """
    
    sum_prices = 0

    for price in prices:
        dis = discount/100
        pricedis = price - price * dis
        print(pricedis)
        sum_prices = sum_prices + pricedis
    print(sum)
    return math.floor(sum_prices)

def main():

    """Main function"""

    discount = 20
    prices = [200, 400, 100]
    price = calculate_total_price(prices, discount)
    print(price)

if __name__ == "__main__":
    main()
