from art import logo



#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Substract
def substract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return round(n1 / n2,2)


operations ={
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}


def calculator():
  print(logo)

  num1 = float(input("Whats's the first number: "))


  for symbol in operations:
    print(symbol)


  continueCalculation = True

  while continueCalculation:
    
    operations_symbol = input("Pick an operation: ")
    num2 = float(input("Whats's the next number: ")) 
    answer = operations[operations_symbol](num1,num2)
    print(f"{num1} {operations_symbol} {num2} = {answer}")
    
    if (input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")).lower() == 'y':
      num1= answer
      continueCalculation = True
    else:
      continueCalculation = False
      calculator()
    
    
calculator()



  



