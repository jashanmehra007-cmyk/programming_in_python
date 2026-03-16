class Employee:
    language = "py"
    salary = 120000

harry = Employee()
harry.name = "Harry" # This is an instance attribute
print(harry.name,harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan robinson"  # This is an instance attribute
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class
