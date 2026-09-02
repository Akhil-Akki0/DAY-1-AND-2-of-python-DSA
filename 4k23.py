price = float(input("Enter the price: "))
discount_rate1 = float(input("Enter the discount rate (in percentage): "))
discount_rate = discount_rate1 / 100

def wrong_discount_calculator(price, discount_rate1):
    discounted_price_2 = price - (price * discount_rate1 / 100)
    return price - (price * discount_rate/100)
print("The discounted price is:", wrong_discount_calculator(price, discount_rate))
def correct_discount_calculator(price, discount_rate1):
    discounted_price_3 = price - (price * discount_rate1 / 100)
    return price - (price * discount_rate/100)
print("The discounted price is:", correct_discount_calculator(price, discount_rate))
#end of the code 
