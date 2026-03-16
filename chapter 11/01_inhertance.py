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

print(a.company, b.company)