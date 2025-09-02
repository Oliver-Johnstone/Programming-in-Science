# Make sure you are not modifying the method signatures
# Function 1: Write a simple Hello World program
# This function should print "Hello, World!" to the screen.
def hello_world():
    # TODO: Implement this function
    print("Hello World!")
    pass  # Replace with your code

# Function 2: Get input and output with different variable types
# This function should prompt the user for their name (string), age (int), and height (float),
# and then print them back in a formatted message.
def input_output():
    # TODO: Implement this function
    name=str(input("Enter your name:"))
    age=int(input("Enter your age:"))
    height=float(input("Enter your height:"))
    print("Hello, "+name+"!")
    print("You are "+str(age)+" years old.")
    print("Your height is "+str(height)+" meters.")
    pass  # Replace with your code
def input_output2():
    name=str(input("Enter your name:"))
    age=int(input("Enter your age:"))
    height=float(input("Enter your height:"))
    print(f"Hello, {name}!")
    print(f"You are {age} years old.")
    print(f"Your height is {height} meters.")
hello_world()
input_output()
input_output2()