# Counting the white space in string 
string = "he leoo lo "
print(string.count(" "))



# Counting Digits, Letters, and Spaces in a string
import re              #Regular expression Library

name = "Hi i am Hamim, 25 years old"

digitCount = re.sub("[^0-9]", "",name)
letterCount = re.sub("[^a-zA-Z]", "",name)
spaceCount = re.findall(r"\s", name)

print("Total Digits = ",len(digitCount))
print("Total Letters = ",len(letterCount))
print("Total Spaces = ",len(spaceCount))

# With out re
name = "Hi i am Hamim, 25 years old"

digit = 0
letter = 0
space = 0

for ch in name:
    if ch.isdigit():
        digit += 1
    elif ch.isalpha():
        letter += 1
    elif ch.isspace():
        space += 1

print("Digits:", digit)
print("Letters:", letter)
print("Spaces:", space)
