#Creating a simple calculater in python

# defining the function to add two numbers
#The second line will return whatever we decided to do; i.e. add/subtract/etc
def add(num1, num2):
	return num1 + num2

# defining the function to subtract two numbers
#The second line will return whatever we decided to do; i.e. add/subtract/etc
def subtract(num1, num2):
	return num1 - num2

# defining the function to multiply two numbers
#The second line will return whatever we decided to do; i.e. add/subtract/etc
def multiply(num1, num2):
	return num1 * num2

# defining the function to divide two numbers
#The second line will return whatever we decided to do; i.e. add/subtract/etc
def divide(num1, num2):
	return num1 / num2

print("Please choose which operation you'd like to do -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


# Below is input from the user through a boolean statement
select = int(input("Select operations from 1, 2, 3, 4 :"))
#int makes all input an integer
#adding the input section allows the user to input with the verbiage within the "" stating what to do

#below defining the functions for the first number adn the second number
#similar to before but with different verbiage/directions
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

#below is the 'if/elif/else' statement which accounts for each of the functions defined above!
if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Not the correct number, please choose from the selection above!")
