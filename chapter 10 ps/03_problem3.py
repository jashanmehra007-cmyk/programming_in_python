class Demo:
    a = 2

o = Demo()
print (o.a) #Prints class attribute because instance attribute is not present
o.a = 0 # Instance attribute is set
print (o.a) # Prints instance attribute because instance attribute is present

