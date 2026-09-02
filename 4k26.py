def is_even (number):
    return number % 2 == 0
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in number:
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
        