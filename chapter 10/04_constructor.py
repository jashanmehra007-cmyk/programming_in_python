<<<<<<< HEAD
class Employee:
    language = "Python"
    salary = 120000

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")
        
    def getinfo(self):
        print(F"The language is{self.language}. The salary is {self.salary}")
    
    @static method

    def greet():
        print("Good morning")

harry = Employee("Harry",130000,"JavaScript")
#harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

rohan = Employee()

=======
class Employee:
    language = "Python"
    salary = 120000

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")
        
    def getinfo(self):
        print(F"The language is{self.language}. The salary is {self.salary}")
    
    @static method

    def greet():
        print("Good morning")

harry = Employee("Harry",130000,"JavaScript")
#harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

rohan = Employee()

>>>>>>> 06e56d1c0f03ad01d4fd6bb656a244e13c3084c1
