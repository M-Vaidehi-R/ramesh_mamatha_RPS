
#defining function winorlose to decide whether to play again or not
def winorlose(status, player, playerlives, computerlives):     

        print("You " + status + "! Would u like to play again?   ")
        Choice = input("Y / N: ")       #user inputs

        if Choice == "n" or Choice == "N":
            print("you chose NO!!!")
            print ("Better luck next time and see you again!!!")
            print("================")
            exit()
            #user input "n", so exiting from the loop (game)

        elif Choice == "y" or Choice == "Y":
            print("you chose YES!!! u r good to gooo!!!!....")
            playerlives = 5
            computerlives = 5
            player = False    
            
            print("***")
            print("**")
            print("*")
            print("**")
            print("***")
            
            #reset and restart game

            #returning values to main_game
            return (playerlives, computerlives, player)