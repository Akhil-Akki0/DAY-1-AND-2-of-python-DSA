def simple_intrest_calucalater(Principal , Rate , Time):
    simple_intrest = (Principal * Rate * Time) / 100
    return simple_intrest
Principal = float(input("Enter the principal amount: "))
Rate = float(input("Enter the rate of interest: "))
Time = float(input("Enter the time period: "))
print("The simple interest is:", simple_intrest_calucalater(Principal,Rate,Time))