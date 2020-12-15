import sys
import math

def calculate_total_price(prices, discount):
    sum = 0 
    for price in prices:
        dis = discount/100
        pricedis = price - price * dis
        print(pricedis)
        sum += pricedis
    print(sum)
    return math.floor(sum)

def main():
    discount = 20
    n = 20
    prices = [200,400,100]
    price = calculate_total_price(prices, discount)
    print(price)

if __name__ == "__main__":
    main()