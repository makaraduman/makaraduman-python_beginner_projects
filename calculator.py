from art import logo
from replit import clear

def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  return a / b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
    print(logo)
    first_num = float(input("What is the first number? "))
    for operation in operations:
        print(operation)
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(first_num, second_num)
        print(f"{first_num} {operation_symbol} {second_num} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            first_num = answer
        else:
            should_continue = False
        clear()
        calculator()

calculator()
