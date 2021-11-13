from gamecomponents import winlose, gameVARS, criteria

# gamecomponents is a folder where winlose, gameVARS, criteria is stored

print("PLAYER LIFE COUNT: " + "(" +str(gameVARS.playerlives) + ")    " + " #" *  (gameVARS.playerlives))        #to show the current score before starting
print("COMPUTER LIFE COUNT: " + "(" + str(gameVARS.computerlives) + ")   " + " #" *  (gameVARS.computerlives))  

# setting up a while loop, to run the game continuosly
while gameVARS.player is False:
    # asking player to choose rock, paper, scissors
    gameVARS.player = input("Choose your weapon: rock, paper or scissors: ")
    print("*****")
    print("player chose: " + gameVARS.player)
    print("computer chose: " + gameVARS.computer)
    print("*****")

    #calling function check from criteria and passing the return value to computerlives and playerlives from gameVARS
  
    gameVARS.playerlives, gameVARS.computerlives =  criteria.check(gameVARS.player, gameVARS.computer,  gameVARS.computerlives, gameVARS.playerlives)      

    print("***")
    print("player life count: " + "(" + str(gameVARS.playerlives) + ")  " + " #" *  (gameVARS.playerlives))
    print("computer life count: " + str(gameVARS.computerlives) + ")   " + " #" *  (gameVARS.computerlives))
    print("***")

    if gameVARS.playerlives == 0:
        #call winorlose here
        winlose.winorlose("lose", 0, 0, 0)
        

    elif gameVARS.computerlives == 0:

        #call winorlose function here
        #returned value of winorlose will go here
        gameVARS.playerlives, gameVARS.computerlives, gameVARS.player = winlose.winorlose("won", gameVARS.player,  gameVARS.computerlives, gameVARS.playerlives ) 
        # will show current score when re-starting   
        print("PLAYER LIFE COUNT: " + "(" + str(gameVARS.playerlives)+")    " + " #" *  (gameVARS.playerlives))
        print("COMPUTER LIFE COUNT: " + "(" + str(gameVARS.computerlives) + ")   " + " #" *  (gameVARS.computerlives))  



    gameVARS.player = False     #making player false, to continue the loop
