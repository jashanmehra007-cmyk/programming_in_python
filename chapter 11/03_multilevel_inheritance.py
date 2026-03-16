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

print(o.a, o.b, o.c)