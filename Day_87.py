# Lambda function

# Addition using lambda
f = lambda a,b : a + b
r = f(10,20)
print(r)

# or 
print(lambda a,b : a+b(4,6))


# Finding factorial using lambda function
f= lambda n : 1 if n == 0 else n*f(n-1)
print(f(5))

"""
if n == 0 → return 1
else → return n × f(n-1)
n! = n × (n-1) × (n-2) × ... × 1
0! = 1
"""


#Square using lambda
square = lambda x: x*x
print(square(4))   # 16



"""
A lambda function is a small, anonymous (nameless) function written in a single line using the lambda keyword.


lambda arguments : expression
"""