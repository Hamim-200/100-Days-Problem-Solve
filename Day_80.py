# Pyramid in Python

def pyramid(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        for j in range(i):
            print("*",end="")
        print("")
pyramid(5)

def pyramid(n):
    for i in range(n):
        print(" " * (n - i) + "*" * (2*i + 1))

pyramid(13)

            
#Diamond in Python
num = int(input("Enter an odd number: "))

# Middle index of the diamond
mid = num // 2

# -------- Upper part of diamond --------
for i in range(mid + 1):
    spaces = mid - i        # Spaces decrease each row
    stars = 2 * i + 1       # Stars increase in odd numbers
    print(" " * spaces + "*" * stars)

# -------- Lower part of diamond --------
for i in range(mid - 1, -1, -1):
    spaces = mid - i        # Spaces increase each row
    stars = 2 * i + 1       # Stars decrease in odd numbers
    print(" " * spaces + "*" * stars)

    