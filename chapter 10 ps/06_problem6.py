from random import randint

class Train:
    def __init__(slf, trainNo): 
     slf.trainNo = trainNo #we can write slf instead of self or we can write any other  word but self is more appropriate

    def book (self, fro, to):
        print(f"Ticket is booked in train no:{self.trainNo} from {fro} to {to}")
        
    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 555)}")

t = Train(12399)
t.book("jalandhar","Delhi")
t.getstatus()

t.getFare("jalandhar","Delhi")        