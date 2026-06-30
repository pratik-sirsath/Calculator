def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed!")
    return a / b

def calc():
    print("================================")
    print("      SIMPLE CALCULATOR")
    print("===============================\n")
    
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    print("\nSelect an operation:")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")

    i = input("\nEnter choice (1/2/3/4): ").strip()

    operation = {
        "1": ("+", add),
        "2": ("-", sub),
        "3": ("*", mul),
        "4": ("/", div),
    }

    if i not in operation:
        print("Error: Invalid choice. Please select 1, 2, 3, or 4.")
        return

    symbol, func = operation[i]

    try:
        result = func(a, b)
        print(f"\nResult: {a} {symbol} {b} = {result}")
    except ValueError as e:
        print(f"\n{e}")

calc()