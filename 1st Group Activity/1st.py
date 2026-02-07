def add(a, b):          # ADDITION
    return a + b

def subtract(a, b):     # SUBTRACTION
    return a - b

def multiply(a, b):     # MULTIPLICATION
    return a * b

def divide(a, b):       # DIVISION
    return a / b


def parse_number(s):

    if "." in s:
        return float(s), False
    else:
        return int(s), True


while True:
    try:
        print("\nSelect operand:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter choice (1/2/3/4): ")

        n1_str = input("Enter first number: ")
        n2_str = input("Enter second number: ")

        num1, is_int1 = parse_number(n1_str)
        num2, is_int2 = parse_number(n2_str)

        both_ints = is_int1 and is_int2

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {int(result) if both_ints else float(result)}")

        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {int(result) if both_ints else float(result)}")

        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {int(result) if both_ints else float(result)}")

        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result: {float(result)}")  # division is always float

        else:
            print("Invalid choice. Please select from 1, 2, 3, 4.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    cont = input("Do you want to perform another calculation? (y/n): ").lower()
    if cont not in ("y", "yes"):
        break

print("Calculator closed.")
