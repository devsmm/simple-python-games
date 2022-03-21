import random

while True:
    userScore = 0
    computerScore = 0
    choices=["rock","scissors","paper"]
    computerChoice=random.choice(choices)
    userChoice=input("rock,paper or scissors:")
    print("computer:"+computerChoice)

    if userChoice.lower()==computerChoice.lower():
            print("Draw")

    if (computerChoice==choices[0] and userChoice.lower()==choices[1]) or\
            (computerChoice==choices[1] and userChoice.lower()==choices[2]) or(computerChoice==choices[2]
            and userChoice.lower()==choices[1]) :
            computerScore+=1
            print("computer wins")
    if (computerChoice == choices[1] and userChoice.lower() == choices[0]) or (
                computerChoice == choices[2] and userChoice.lower() == choices[1]) or (
                computerChoice == choices[1] and userChoice.lower() == choices[2]):
            userScore += 1
            print("user wins")

    print("user:"+str(userScore))
    print("computer:"+str(computerScore))
    quitMessage = input("Press q to quit or any key to play again:")
    if quitMessage.lower() == "q":
        break
