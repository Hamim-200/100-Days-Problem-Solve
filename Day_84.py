# Creating instance member variable in python

class Test:
    def __init__(self):
        self.a = 5          # instance variable created for every object

    def f1(self):
        self.b = 10         # instance variable created only when f1() is called

t1 = Test()
t2 = Test()

t1.f1()

print(t1.__dict__)
print(t2.__dict__)



# self.a = 5 → created in __init__ → every object gets a

# self.b = 10 → created inside f1() → only objects that call f1() get b

# t1.f1() is called → only t1 gets variable b

# t2.f1() is NOT called → t2 does not have b