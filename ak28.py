def power(base, exponent=2):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
print("=" * 50)
print("DEMONSTRATING THREE CALLING STYLES")
print("=" * 50)
print("\n1. DEFAULT ARGUMENT STYLE:")
print("   power(5) - uses default exponent=2")
print(f"   Result: {power(5)}")  # 5^2 = 25
print()
print("2. POSITIONAL ARGUMENTS STYLE:")
print("   power(3, 4) - base=3, exponent=4")
print(f"   Result: {power(3, 4)}")  # 3^4 = 81
print()
print("3. KEYWORD ARGUMENTS STYLE:")
print("   power(base=2, exponent=6) - using keyword arguments")
print(f"   Result: {power(base=2, exponent=6)}")  # 2^6 = 64
print()
print("=" * 50)
print("ADDITIONAL EXAMPLES")
print("=" * 50)
print("\nDefault argument (squaring):")
print(f"  power(4) = {power(4)}")        # 4^2 = 16
print(f"  power(10) = {power(10)}")      # 10^2 = 100
print(f"  power(2.5) = {power(2.5)}")    # 2.5^2 = 6.25
print("\nPositional arguments:")
print(f"  power(2, 8) = {power(2, 8)}")          # 2^8 = 256
print(f"  power(5, 3) = {power(5, 3)}")          # 5^3 = 125
print(f"  power(10, 0) = {power(10, 0)}")        # 10^0 = 1
print("\nKeyword arguments:")
print(f"  power(exponent=5, base=3) = {power(exponent=5, base=3)}")  # 3^5 = 243
print(f"  power(base=7, exponent=2) = {power(base=7, exponent=2)}")  # 7^2 = 49
print(f"  power(exponent=3, base=4) = {power(exponent=3, base=4)}")  # 4^3 = 64
print("\nMixed style (positional + keyword):")
print(f"  power(5, exponent=3) = {power(5, exponent=3)}")  # 5^3 = 125