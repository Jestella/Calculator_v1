# Simple calculator

# This function adds two numbers
def add(x,y):
  return x + y

# This function subtracts two numbers
def subtract(x,y):
  return x - y

# This functions multiplies two numbers
def multiply(x,y):
  return x * y

# This function divides two numbers
def divide(x,y):
  return x / y

print("Select operation")
print("A.Add")
print("B.Subtract")
print("C.Multiply")
print("D.Divide")

while True:
   # Take input from the UserWarning
   choice = input("Enter choice(A/B/C/D): ")

   # Check if choice is one of the four options
   if choice in ('A','B','C','D'):
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))

     if choice == 'A':
       print(num1, "+", num2, "=", add(num1, num2))
     elif choice == 'B':
       print(num1, "-", num2, "=", substract(num1, num2))
     elif choice == 'C':
       print(num1, "*", num2, "=", multiply(num1, num2))  
     elif choice == 'D':
       print(num1, "/", num2, "=", divide(num1, num2))
   else:
     print("Invalid Input")



