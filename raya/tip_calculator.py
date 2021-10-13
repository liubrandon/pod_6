def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():

  num1 = float(input("What's the price of your meal?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation, * for percentage tip, + to add an amount or / to divide the bill equally: ")
    num2 = float(input("Tip amount (in whole numbers), percentage (ex. 0.15 for 15 percent or 0.09 for 9 percent) or how many people will be paying (dividing amongst you using whole numbers?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with your current calculation {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      print('Thank you for choosing MoooMooo Dining')
      
      calculator()

calculator()