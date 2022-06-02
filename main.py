import random

while True:
    option =["rock","paper","scissors"]

    computer = random.choice(option)
    player = None

    while player not in option:
        player = input("Rock, Paper or Scissors \n\n Choice: ").lower()


    if player == computer:
        txt = "player({0}):CPU({1})"
        print(txt.format(player,computer))
        print("Tie!")
        
        
    elif player == "rock":
        if computer == "paper":
            txt = "Player({0}):CPU({1})"
            print(txt.format(player,computer))
            print("CPU wins")
            break
        if computer == "scissors":
            txt = "Player({0}):CPU({1})"
            print(txt.format(player,computer))
            print("You win")
            break

    elif player == "scissors":
        if computer == "rock":
            txt = "Player({0}):CPU({1})"
            print(txt.format(player,computer))
            print("CPU wins")
            break
        if computer == "paper":
            txt = "Player({0}):CPU({1})"
            print(txt.format(player,computer))
            print("You win")
            break

    elif player == "paper":
        if computer == "scissors":
            txt = "Player({0}):CPU({1})"
            print(txt.format(player,computer))
            print("CPU wins")
            break
        if computer == "rock":
            txt = "Player({0}):CPU({1})"
            print(txt.format(player,computer))
            print("You win")
            break
        

