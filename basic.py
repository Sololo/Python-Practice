# """
# Program : Miles to Kilometers converter
# kilometers = miles * 1.60934

# Enter Miles 5
# 5 miles equals 8.04 km

# """
# miles = input('Enter Miles ')
# miles = int(miles)
# converter = 1.60934

# kilometers = miles * converter

# print("{} Miles = {} Kilometers".format(miles, kilometers))



# """
# Program calculator

# Store the user input of 2 numbers and the operatot
# Convert the strings into intergers
# Calculation based on operator input

# Print the result
# """
# num1, operator, num2 = input('Enter Calculation ').split()

# num1 = int(num1)
# num2 = int(num2)

# if operator == "+":
#     print("{} + {} = {}".format(num1, num2, num1 + num2))
# elif operator == "-":
#     print("{} - {} = {}".format(num1, num2, num1 - num2))
# elif operator == "*":
#     print("{} * {} = {}".format(num1, num2, num1 * num2))
# elif operator == "/":
#     print("{} / {} = {}".format(num1, num2, num1 / num2))
# else:
#     print("Use either: + - * or / next time")



# """
# Program looks for odd numbers from a sample space 

# Use for loop through the list from 1 to 21
# Use modulus to check that the result is NOT EQUAL to 0

# Print the odds
# """
# for i in range(1, 21):
#     if ((i % 2) != 0):
#         print("i = ", i)



# """
# Floating numbers
# """
# your_float = input("Enter a float: ")
# your_float = float(your_float)
# print("Round to 2 decimals: {:.2f}".format(your_float))



"""
Exeption Handling

"""

while True:

    try:
        number = int(input("Please enter a number : "))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unkown error occured")

print("Thank you for entering a number")