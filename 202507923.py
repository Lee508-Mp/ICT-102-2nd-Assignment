"""Function defines the formula to use when finding the nth Fibonacci number. The main function handles user input and displays the result."""
def fibonacci_recursive(n: int) -> int:
    """Returns the nth Fibonacci number using recursion."""
        # Base case: F(0) = 0
    if n == 0:
        return 0
    # Base case: F(1) = 1
    elif n == 1:
        return 1
    # Recursive case: apply the formula F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

