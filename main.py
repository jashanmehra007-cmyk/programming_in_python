import random
'''
snake = 1
water = -1
gun = 0
'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s": 1,"w": -1,"g": 0}
reverseDict = {1:"Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have two numbers(variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose{reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you ==1 ):
        print("You win") 

    elif(computer ==-1 and you ==0):
        print("You lose!")

    elif(computer ==1 and you ==-1):
        print("You lose!")

    elif(computer ==1 and you ==0):
        print("You win")

    elif(computer ==0 and you ==-1):
        print("You win")

    elif(computer ==0 and you ==1):
        print("You lose!")

    else:
        print("Something went wrong!")

   


