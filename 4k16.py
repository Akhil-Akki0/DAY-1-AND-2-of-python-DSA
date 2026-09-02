attempts = 0
while attempts <3:
    pin = input("enter the pin:")
    if pin == "1234":
        print("access granted")
        break
        attempts += 1
    
else:
    print("your account has been locked")