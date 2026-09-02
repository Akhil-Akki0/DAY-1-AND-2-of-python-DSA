def calucalate_simple_interest(Principal, Rate, Time):
    simple_interest = (Principal * Rate * Time) / 100
    return simple_interest
intrest1=calucalate_simple_interest(10000, 5, 2)
intrest2=calucalate_simple_interest(20000, 7, 3)
print("The simple interest for the first case is:", intrest1)
print("The simple interest for the second case is:", intrest2)