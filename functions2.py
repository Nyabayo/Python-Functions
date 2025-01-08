#Functions:
#A function is a block of code that performs a specific function.
# You define a function once and use it multiple times in your code.
#Syntax
# def function_name(parameters):
#optional docstring explaining the function.
#code block
#return value also optional
# Types of Functions
# Built-in Functions: Predefined functions in Python (e.g., print(), len(), type()).
# User-defined Functions: Functions created by the user.
# Defining and Calling a Function
def my_name(name):
    print(name)
my_name("Ernest")

def greetings(name):
    print(f"How are you {name}?")

greetings("Ernest")

#Function definition
def greet(name):
    return f"Hello, {name}!"
#function call
print(greet("Elvis"))

