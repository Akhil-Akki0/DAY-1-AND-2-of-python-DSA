word = input("enter the word:")
word = word.lower()
reverse_word = word[::-1]
if word == word[::-1]:
    print("REVERSE:", reverse_word)
    print("it is a palindrome")
else:
    print("REVERSE:", reverse_word)
    print("it is not a palindrome")