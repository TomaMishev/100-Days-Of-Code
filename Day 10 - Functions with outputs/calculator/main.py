from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    operations = {"+": add,
                  "-": subtract,
                  "*": multiply,
                  "/": divide,
                  }
    is_running = True
    print(logo)
    num1 = float(input("Whats the first number?: "))
    for key in operations:
        print(key)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Whats the next number?: "))
    calculation_function = operations[operation_symbol]
    result = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    user_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation.: ")
    while is_running:
        if user_input == 'n':
            is_running = False
            calculator()
        operation_symbol = input("Pick another operation: ")
        num3 = float(input("What's the next number: "))
        calculation_function = operations[operation_symbol]
        second_result = calculation_function(result, num3)

        print(f"{result} {operation_symbol} {num3} = {second_result}")
        user_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation.: ")


calculator()
