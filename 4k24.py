def celsius_to_faranheat(celsius):
    faranheat = (celsius * 9/5) + 32
    return faranheat
def get_temperature_input(celsius):
    fahrenheit = celsius_to_faranheat(celsius)
    if fahrenheit >= 100:
       return"The temperature is heigh."
    elif fahrenheit <= 50:  # 50 Celsius in Fahrenheit
       return"The temperature is too low."
    else:
       return "The temperature is good enjoy today."
climate_temparature = float(input("Enter the temperature in Celsius: "))
topic = get_temperature_input(climate_temparature)
print( topic)
