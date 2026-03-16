class Employee:
    language = "py"
    salary = 150000
    
    def getinfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")
harry= Employee()
# harry = "java script"
harry.getinfo()