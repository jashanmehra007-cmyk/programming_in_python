<<<<<<< HEAD
class Employee:
    def __init__(self):
        print("Constructer of Employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
        print("Constructer of Programmer")
    b = 2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructer of Manager")
    c = 3

# o = Employee()
# print(o.a) #prints the attribute   

# o = Programmer()
# print(o.a, o.b)

o = Manager()
=======
class Employee:
    def __init__(self):
        print("Constructer of Employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
        print("Constructer of Programmer")
    b = 2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructer of Manager")
    c = 3

# o = Employee()
# print(o.a) #prints the attribute   

# o = Programmer()
# print(o.a, o.b)

o = Manager()
>>>>>>> 06e56d1c0f03ad01d4fd6bb656a244e13c3084c1
print (o.a , o.b , o.c)