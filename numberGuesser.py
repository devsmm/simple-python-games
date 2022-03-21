import random
print("Guess the number from 1 to 20")
randomNumber=random.randint(1,20)
trials=1

while True:
    userNumber = input("Enter your guess:")
    if int(userNumber)>0<21:
        if int(userNumber)==randomNumber:
            print("Correct Guess.")
            print("You have guessed it in "+str(trials)+" turns")
            break
        else:
            if int(userNumber)<randomNumber:
                print("Higher")
            if int(userNumber)>randomNumber:
                print("lower")
            print("Try again")
            trials+=1
    else:
        print("Enter valid number between the specified values")


