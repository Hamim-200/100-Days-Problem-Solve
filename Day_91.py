"""
Type Conversion

> Type conversion means changing one data type into another.

> String → Integer
> Integer → Float
> Float → String

Why We Need Type Conversion?
> Sometimes Python cannot perform operations between different types.
"""

# 🔹 Implicit Type Conversion
a = 5          # int
b = 2.5        # float
c = a + b      # int automatically converts to float
print("Implicit:", c, type(c))


# 🔹 String → Integer
x = "10"
y = int(x)
print("String to Int:", y, type(y))


# 🔹 Integer → String
n = 50
s = str(n)
print("Int to String:", s, type(s))


# 🔹 Float → Integer
f = 5.9
i = int(f)     # decimal part removed
print("Float to Int:", i, type(i))


# 🔹 String → Float
sf = "3.14"
ff = float(sf)
print("String to Float:", ff, type(ff))


# 🔹 String → List
word = "hello"
lst = list(word)
print("String to List:", lst, type(lst))


# 🔹 List → Tuple
my_list = [1, 2, 3]
t = tuple(my_list)
print("List to Tuple:", t, type(t))


# 🔹 List → Set
my_list2 = [1, 2, 2, 3]
st = set(my_list2)
print("List to Set:", st, type(st))


# 🔹 Boolean Conversion
print("Bool(0):", bool(0))
print("Bool(1):", bool(1))
print("Bool(''):", bool(""))
print("Bool('Hello'):", bool("Hello"))