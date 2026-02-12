def factorial(n):
    """Compute the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <non-negative integer>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        result = factorial(num)
        print(f"The factorial of {num} is {result}.")
    except ValueError as e:
        print(e)
        sys.exit(1)