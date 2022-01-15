#ROCK, PAPER, SCISSORS GAME
import random
print("| Rock Paper Scissors |")
listCh = ["R", "P", "S"]
Akshitha = 0
computer = 0
i = 1
chance = int(input("How many time you want to play: "))


class AkshithaCh:
    pass


while i <= chance:
    computerCh = str(random.choice(listCh))
    AkshithaCh = input("Enter Rock, Paper, Scissors (key to press: R,P,S): ").upper()
    if AkshithaCh == computerCh:
        print("Tie You Both Entered Same")
    elif AkshithaCh == "R":
        print("Computer Enter: ", computerCh)
        if computerCh == "P":
            print(" You lost! Paper covers Rock")
            computer += 1
        else:
            print("You won! Rock smashes Scissors")
            Akshitha += 1
    elif AkshithaCh == "P":
        print("Computer Enter: ", computerCh)
        if computerCh == "S":
            print("You lost! Scissor cuts Paper")
            computer += 1
        else:
            print("You won! Paper covers Rock")
            Akshitha += 1
    elif AkshithaCh == "S":
        print("Computer Enter: ", computerCh)
        if computerCh == "R":
            print("You lost! Rock smashes Scissors")
            computer += 1
        else:
            print("👉 You win! Scissor cut Paper")
            Akshitha += 1
    else:
        print(":(")
    print("\n\t******ScoreBoard******")
    print(f"\t You: {Akshitha} | Computer: {computer}")
    print("\t**********************")
    print(f"Game No:[{i}]")
    print("========================================================")
    i += 1
print("\n\n##### Game Over #####")
print("*******************************************")
if Akshitha < computer:
    print(
        "Sorry You lost the game\n computer win the game with score:", computer
    )
elif Akshitha == computer:
    print(" Tie !! Play Again ")
else:
    print("You Won the Game with score:", Akshitha)
