# class Number:
#     n = 14

# print(Number.n)    

class Number:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f"Number is {self.n}"
    
n1 = Number(14)
n2 = Number(18)

print(n1)
print(n2)    
