units = int(input("enter the units:"))
if units <= 100:
    bill = units *5
else:
    bill = (100 * 5) + ((units - 100) * 7)
print(f"total bill: Rs{bill:.2f}")
print(f"units consumed: {units}")
