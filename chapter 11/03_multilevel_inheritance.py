<<<<<<< HEAD
class Employee:
    a = 1

class programmer(Employee):
    b = 2

class Manager(programmer):
    c = 3        

o = Employee()
print(o.a) # Prints the a attribute
#print(o.b) # Shows an error as there is no b attribute in Employee class

o = programmer()
print(o.a, o.b)

o = Manager()
=======
class Employee:
    a = 1

class programmer(Employee):
    b = 2

class Manager(programmer):
    c = 3        

o = Employee()
print(o.a) # Prints the a attribute
#print(o.b) # Shows an error as there is no b attribute in Employee class

o = programmer()
print(o.a, o.b)

o = Manager()
>>>>>>> 06e56d1c0f03ad01d4fd6bb656a244e13c3084c1
print(o.a, o.b, o.c)