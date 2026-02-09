# Implementing variable length arguments in Python

def average(*t):
    
    if len(t) == 0:
        return 0
    avg = sum(t)/len(t)
    return avg 

result1 = average(10,20,30,50,0,1001)

print(result1)

# *t collects any number of inputs into a tuple
# sum(t) adds them
# len(t) counts them