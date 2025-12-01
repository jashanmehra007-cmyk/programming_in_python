a = int(input("Enter your age"))

#IF statement No.1
if(a%2 ==0):
    print("a is even")

#IF statement No.2    
if(a>=18):
    print("You are above the age of consent")
    print("you are eligible")

elif(a>0):
    print("You are entering invalid negative age")

else:
    print("you are below the age of consent")

print("End of program")
