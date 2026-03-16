<<<<<<< HEAD
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n 

n = Number(1)
m = Number(2)

=======
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n 

n = Number(1)
m = Number(2)

>>>>>>> 06e56d1c0f03ad01d4fd6bb656a244e13c3084c1
print(n + m)