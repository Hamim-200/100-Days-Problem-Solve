# FIBONACCI Series
# The Fibonacci series is a sequence of numbers where each number is the sum of the two numbers before it.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

n = 10 #how many numbers i want
a,b = 0,1 # First two numbers of the series

for i in range(n):
    print(a, end = " ") #print current number and space

    c = a + b
    a = b # move forward: a becomes b
    b = c # move forward: b becomes sum of previous two
