<<<<<<< HEAD
class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n*self.n**1/2}")
    
    @staticmethod
    def hello():
        print("Hello there!")

a = calculator(12)  
a.hello()
a.square() 
a.cube()
a.squareroot()                                    

=======
class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n*self.n**1/2}")
    
    @staticmethod
    def hello():
        print("Hello there!")

a = calculator(12)  
a.hello()
a.square() 
a.cube()
a.squareroot()                                    

>>>>>>> 06e56d1c0f03ad01d4fd6bb656a244e13c3084c1
