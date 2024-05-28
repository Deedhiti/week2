#python program for simple calculator

#function to add two numbers
def addition(n1, n2):
    return n1 + n2

#function to substract two numbers
def subtraction(n1,n2):
    return n1 - n2;

#function to multiply two numbers
def multiplication(n1,n2):
    return n1 * n2;

#function to divide two numbers
def division(n1,n2):
    return n1 / n2;

print("Select the desired operation -\n" \
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")
choice = int(input("Select the desired operation form 1, 2, 3, 4 :"))
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if choice == 1:
    print(number1, "+", number2, "=", addition(number1,number2))

elif choice == 2:
    print(number1, "-", number2, "=", subtraction(number1,number2))

elif choice == 3:
    print(number1, "*", number2, "=", multiplication(number1,number2))

elif choice == 4:
    print(number1, "/", number2, "=", division(number1,number2))

else:
    print("Invalid Input! Please Try Again.")

