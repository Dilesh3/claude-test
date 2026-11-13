def factorial(n: int) -> int:
    """Return n! for a non-negative integer n."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer: "))
        print(f"{n}! = {factorial(n)}")
    except ValueError as e:
        print(f"Error: {e}")
