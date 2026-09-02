# ============================================
# STEP 1: Create global variable
# ============================================
counter = 0

# ============================================
# STEP 2: Function that causes UnboundLocalError
# ============================================
def increment_broken():
    """
    This function attempts to modify the global variable 'counter'
    WITHOUT using the 'global' keyword.
    
    PREDICTION: This will raise an UnboundLocalError
    """
    counter += 1  # This line will cause an error
    return counter

print("=" * 60)
print("DEMONSTRATING THE ERROR")
print("=" * 60)
print(f"Initial counter value: {counter}")

# Try to call the broken function (commented out to prevent script crash)
# Uncomment the line below to see the error in action
# print(f"Trying to increment: {increment_broken()}")

"""
EXPLANATION OF THE ERROR:
-------------------------
When Python sees 'counter += 1' inside the function, it does the following:

1. Python assumes 'counter' is a LOCAL variable because we're assigning to it
2. It looks for a local variable 'counter' - but none exists yet
3. It tries to read the current value of 'counter' to add 1 to it
4. Since no local 'counter' exists, it raises UnboundLocalError

The error message would be:
UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value

Even though there's a GLOBAL variable named 'counter', Python creates a LOCAL
variable when we assign to it inside the function. The assignment happens
after the read operation, causing the error.
"""

print("\n" + "=" * 60)
print("THE FIX: Using the 'global' keyword")
print("=" * 60)

# ============================================
# STEP 3: Fixed version with 'global' keyword
# ============================================
def increment_fixed():
    """
    This function correctly modifies the global variable 'counter'
    using the 'global' keyword.
    """
    global counter  # Declare that we want to use the global 'counter'
    counter += 1    # Now this modifies the global variable
    return counter

# Test the fixed function
print(f"Before increment: counter = {counter}")
result = increment_fixed()
print(f"After increment:  counter = {counter}")
print(f"Returned value:   {result}")

# Call it multiple times to show it works
print("\nCalling increment_fixed() multiple times:")
for i in range(1, 6):
    increment_fixed()
    print(f"  After call {i}: counter = {counter}")

# ============================================
# STEP 4: Alternative - Using a list (workaround)
# ============================================
print("\n" + "=" * 60)
print("ALTERNATIVE WORKAROUND: Using a mutable container")
print("=" * 60)

# You can also use a mutable container like a list
counter_list = [0]

def increment_with_list():
    """Increments counter using a list (no global keyword needed)"""
    counter_list[0] += 1
    return counter_list[0]

print(f"Initial counter_list: {counter_list[0]}")
increment_with_list()
print(f"After increment: {counter_list[0]}")
increment_with_list()
print(f"After second increment: {counter_list[0]}")

# ============================================
# STEP 5: Reading global variable (no global needed)
# ============================================
print("\n" + "=" * 60)
print("READING A GLOBAL VARIABLE (No 'global' needed)")
print("=" * 60)

def read_counter():
    """
    This function reads the global variable 'counter'
    WITHOUT using the 'global' keyword - this is fine!
    """
    return counter  # Reading is allowed without 'global'

print(f"Reading global counter: {read_counter()}")  # No error!

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
RULE: 
- You DON'T need 'global' to READ a global variable
- You DO need 'global' to MODIFY (assign to) a global variable

WHY?
- Python creates local variables by default when you assign inside a function
- 'global' tells Python to use the global variable instead
- Without 'global', Python thinks you're creating a new local variable
  and gets confused when you try to read before assigning

FIX:
Use 'global variable_name' at the start of your function
before any operations that modify the global variable.
""")