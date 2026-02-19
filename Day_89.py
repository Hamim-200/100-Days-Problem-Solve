# what is the use of split and join function of str ?

# split() and join() in Python (String Methods) These two functions are used for breaking strings and combining strings.


# split() → Break a String into a List
text = "I love Python"
words = text.split()
print(words)

data = "apple,banana,mango"
result = data.split(",")
print(result)

# join() → Combine List into a String
words = ['I', 'love', 'Python']
sentence = " ".join(words)
print(sentence)

items = ['apple', 'banana', 'mango']
result = "-".join(items)
print(result)
