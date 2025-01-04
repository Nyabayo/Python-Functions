#Python Functions
#A function is a block of code which only runs when it is called.
#You can pass data known as parameter, into a function.
#A function can return data as a result.
#Creating a function
#Defined using the (def) keyword.
#example 1
# def my_function():
#     print("Hello from a function")

#Calling a function
def my_function():
    print("My first function")
my_function()

#Arguments
#Information can be passed into a function as arguments.
#Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them using a comma.
#Create a function with one argument (fname).
#When the function is called, we pass along a first name, which is used inside the function to print the full name.
#example
def add_argument(fname):
    print(fname +  " "  "Osindo")
add_argument("Ernest")

#Example2
def argument(name): #name is a parameter
    print(f"Her name is {name}")
argument("Favour Gatwiri") #Favour Gatwiri is an argument

#Arguments are often shortened to args in python documentation
# Parameters or Arguments
#Both paramenters and arguments are used for the same thing: Information that is passed to a function.
#From afunction's perspective:
#A parameter is a variable listed inside the parentheses in the function definition.
#An Argument is the value that is sent to the function once the Function is called.

#Number of arguments
#Create a function with two parameters.
def two_parameters(fname, lname):
    print(fname + " " + lname)
two_parameters("Elvis", "Osindo")
#If a function expects two arguments, then they must be passed during  function call otherwise it will throw an error.



#Arbitrary Arguments, *args
#If you don't know how many arguments that will be passed into you function, add a * before the parameter name in the function definition
# THis way the function will receive a tuple of arguments, and can access the items accordingly.
def arbitrary_arguments(*kids):
    print("The youngest kid is" + " " + kids[2])
arbitrary_arguments("Magda", "Kerubo", "Gatwiri")

#NOTE: Arbitrary Arguments are often shortened to *args in Python documentations.
#Keyword Arguments
#This way the order of the arguments does not matter.
def keyword_arguments(girl1, girl2, girl3):
    print("The most beautiful girl is" + " " + girl1)
keyword_arguments(girl1= "Linet", girl2= "Gatwiri", girl3= "Cate")
# The phrase Keyword Arguments are often shortened to kwargs in python documentation.


#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
def arbitrary_keyword_arguments(**girl):
    print("The virgin girl is" + " " + girl["girl2"])
arbitrary_keyword_arguments(girl1 = "Linet", girl2 = "Gatwiri", girl3 = "Cate")
#Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentations.

# Default parameter value
#If we call the function without argument, it uses the default value:
def default_parameter_value(contry = "Kenya"):
    print("I am from " + " " + contry + ".")
default_parameter_value()
default_parameter_value("Rwanda")

#Passing a list as an argument
#You can send any data types  of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def list_argument(food):
    for x in food:
        print(x)
fruits = ["apple", "lemon", "orange", "avocado"]
list_argument(fruits)

def list_argument2(food):
    for x in food:
        print(x)
veges = ["Cabbage", "Sukuma", "Boga", "pumbkin leaves", "pig weed"]
list_argument2(veges)

#Return Values
#To let a function return a value, use the return statement:
def return_values(x):
    return 5 * x
print(return_values(5))

#The pass statement
#Function definitions cannot be empty, but  if you for some reason have a function with no content , put in the pass statement to avoid getting an error.
def x():
    pass


#Positional-Only Arguments
#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the argument
def positional_only_arguments(x, /):
    print(x)
positional_only_arguments(3)
#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
# def positional_only_arguments(x):
#     print(x)
# positional_only_arguments(x = 7)

#Keyword-Only Arguments
#To specify that a function can have only keyword arguments, add *, before the arguments:
def keywords_only_arguments(*, y):
    print(y)
keywords_only_arguments(y = 8)

#Combine Positional-Only and Keyword-Only
#You can combine the two argument types in the same function.
#Any argument before the / , are the positional-only, and any argument after the * , are keyword-only
def position_keyword(a, b, /, *, c, d):
    print(a + b + c + d)
position_keyword(5, 6, c = 7, d = 8)

def combine_positional_keyword_arguments(q, w, e, /, *, r, t, y):
    print(q + w + e + y)
combine_positional_keyword_arguments(4,5,6, r=7,t=8,y=9)

#Recursion
#Recursion means that a function can call itself
# Recursion is common in mathematical and programming concept.
#It means that a function can call itself.
#THis has the benefit of meaning that you can loop through data to reach a result.
#A developer should be careful eith recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power.
#However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
#In this example, tri_recursion() is a function that I have defined to call itself("recurse").
#We use the k variable as the data, which decrements (-1) every time we recurse.
#The recursion ends when the condition is not greater than 0 (i.e. when it is 0),.
#To a new developer it can take some time to work out how exactly this works.
#The best way to find to find out is by testing and modifying it.
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Example Result:")
tri_recursion(6)










