magic_number = 12
attempts = 0
while True:
    guess = input("guess the magic number (hint: it's a 2-digit number) OR type QUIT :")
    
    if guess == magic_number:
        print("congratulations! you guessed it right")
        print(f"you guessed it in {attempts + 1} attempts")
        break
    else:
        print("wrong guess! try again")
        attempts += 1