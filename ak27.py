# write a function called max of three (abc) 
# that returns the largest of three numbers only if / else /ifesle
# (no -build in max())then test it with three different set of numbers
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("Test 1: max_of_three(5, 2, 8)")
print(f"Result: {max_of_three(5, 2, 8)}")  
print()
