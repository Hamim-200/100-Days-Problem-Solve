# Local and Global variable in Python

"""
> Variables in Python can have different scopes depending on where they are created.
> A local variable is created inside a function and can only be used inside that function.
> A global variable is created outside any function and can be used anywhere in the program.
""" 

# Local Variable
def test():
    x = 10   # local variable
    print(x)

test()


# Global Variable
x = 20   # global variable

def test():
    print(x)

test()


# Modifying Global Variable Inside Function
x = 10

def test():
    x = 5
    print(x)

test()
print(x)

# Outputs are 5, 10 Because x = 5 creates a new local variable, not modifying the global one.

# To Modify Global Variable → Use global Keyword
x = 10

def test():
    global x
    x = 5

test()
print(x)