<<<<<<< HEAD
class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.salary}")

# class programmer:
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
#     def show(self):
#         print(f"The name of Employee is {self.name} and the salary is {self.salary}")

class programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = programmer()

=======
class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.salary}")

# class programmer:
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
#     def show(self):
#         print(f"The name of Employee is {self.name} and the salary is {self.salary}")

class programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = programmer()

>>>>>>> 06e56d1c0f03ad01d4fd6bb656a244e13c3084c1
print(a.company, b.company)