b = "banana,dog , bananadog@gmeil.com"
print(b)
cleaned = b.strip()
parts = cleaned.split(",")
print(cleaned.split(","))
print(cleaned.split(" "))

first_name = parts[0]
last_name = parts[1]
gmail = parts[2]
full_name = " ".join([first_name, last_name])
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")