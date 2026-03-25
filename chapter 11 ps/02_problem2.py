class animals:
    pass

class pet(animals):
    pass

class dog(pet):
    @staticmethod 
    def Bark():
        print("Bow Bow!!")

d = dog()
d.Bark()