#defining function "check" for comparing the code and getting the result

def check(player, computer, computerlives, playerlives):
    
    #if the player lose, player lose one point and if computer loses the vice versa
    
    if computer == player:
        # tie - nothing else to compare, so it'll pass
        print("tie! try again")
        print("-----")

    elif player == "rock":
        if computer == "paper":
            print("you lose! :( ")
            print("-----")
            playerlives = playerlives - 1
        else:
            print("you win! :) ")
            print("-----")
            computerlives = computerlives - 1

    elif player == "paper":
        if computer == "scissors":
            print("you lose! :( ")
            print("-----")
            playerlives = playerlives - 1
        else:
            print("you win! :) ")
            print("-----")
            computerlives = computerlives - 1

    elif player == "scissors":
        if computer == "rock":
            print("you lose! :( ")
            print("-----")
            playerlives = playerlives - 1
        else:
            print("you win! :) ")
            print("-----")
            computerlives = computerlives - 1

    #returning the value to main_game
    return (playerlives, computerlives)