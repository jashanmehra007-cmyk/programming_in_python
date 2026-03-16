class programmer:
    company = "Microsoft"
    def __init__(self, name, salary,language):
        self.name = name
        self.salary = salary 
        self.language = language
p = programmer("jashan",120000,"Python")
print(p.name, p.salary, p.language,p.company)

r = programmer("simran",130000,"Java script")
print(r.name, r.salary, r.language,r.company)