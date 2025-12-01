n = int(input("Enter a number: "))

for i in (2,n):
    if(n%i) == 0:
        print("This number is not prime. ")
        break

else:
    print("This number is prime")



