def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	if y == 0:
		return "Error: Division by zero is not allowed"
	return x / y
num1 = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
# Perform the calculation based on the user's choice
if operation == "+":
	result = add(num1, num2)
elif operation == "-":
	result = subtract(num1, num2)
elif operation == "*":
	result = multiply(num1, num2)
elif operation == "/":
	result = divide(num1, num2)
else:
	result = "Error: Invalid operation choice"
# Display the result
print("The result is: ", result)
