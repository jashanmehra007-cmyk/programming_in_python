<<<<<<< HEAD
class Employee:
    a = 1 
    @classmethod 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.ename} {self.name}"
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    
e = Employee()
e.a = 45

e.name = "Jashan mehra"
print(e.fname, e.lname)

=======
class Employee:
    a = 1 
    @classmethod 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.ename} {self.name}"
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    
e = Employee()
e.a = 45

e.name = "Jashan mehra"
print(e.fname, e.lname)

>>>>>>> 06e56d1c0f03ad01d4fd6bb656a244e13c3084c1
e.show()