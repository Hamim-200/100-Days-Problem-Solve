# List Comprehension in Python
"""
List comprehension is a short and clean way to create a new list using a single line of code instead of writing a full loop.

[expression for item in iterable]
"""

square = [x*x for x in range(5)]
print(square)


evens = [x for x in range(10) if x % 2 == 0]
print(evens)

labels = ["even" if x%2==0 else "odd" for x in range(5)]
print(labels)


# create a list of even number from a given list
nums = [1, 2, 3, 4]
lst = [x for x in nums if x%2==0]
print(lst)