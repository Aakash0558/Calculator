from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def sub(n1, n2):
  return n1 - n2

#Multiply
def mul(n1, n2):
  return n1 * n2

#Division
def div(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,
}

def calculator():
  
  print(logo)
  
  num1 = float(input("Enter a number? "))                   #take one input
  
  for sign in operations:                                   #loop through operations
    print(sign)
  
  first_cont = True
  
  while first_cont:
    operation_sign = input("Pick an operation: ")           #take operation symbol input
    
    if operation_sign in operations:                        #if the signs match, program executes; else, try proper input
      num2 = float(input("Enter next number? "))            #take another input when operation sign matches 
      calculation_function = operations[operation_sign]
      first_answer = calculation_function(num1, num2)       #calling the functions
      
      print(f"{num1} {operation_sign} {num2} = {first_answer}")
     
     #choice to end the program
      choice1 = input(f"Type 'y' to keep calculating, or type 'n' to end the program:\n").lower() 
      if choice1 == "n":
        first_cont = False
      else: 
        #continue with the answer or start fresh calculation
        choice2 = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation:\n").lower()   
        if choice2 == "n":
          first_cont = False
          calculator()                                      #recursion
        elif choice2 == "y":
          num1 = first_answer
    
    else:
      print("Wrong operation! Try again.")
    
    
calculator()
