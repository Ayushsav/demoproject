def sum_of_two_numbers(a, b):
    return a + b

# Example usage
if __name__ == "__main__":
    num1 = 5
    num2 = 3
    result = sum_of_two_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
    
    # Additional enhancement: handling user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = sum_of_two_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")