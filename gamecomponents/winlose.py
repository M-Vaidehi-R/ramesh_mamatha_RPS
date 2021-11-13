
#defining function winorlose to decide whether to play again or not
def winorlose(status, player, playerlives, computerlives):     
                      
        print("You " + status + "! Would u like to play again?   ")
        Choice = input("Y / N")       #user inputs

        if Choice == "n" or Choice == "N":
            print ("Better luck next time and see you again!!!")
            exit()
            #user input "n", so exiting from the loop (game)

        elif Choice == "y" or Choice == "Y":
            print("good to gooo....")
            #reset and restart game

            playerlives = 2
            computerlives = 2
            player = False    

            #returning values to main_game
            return (playerlives, computerlives, player)