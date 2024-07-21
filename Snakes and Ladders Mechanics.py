#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#IMPORT SECTION
import time
import turtle
import random
import Board
Board.GameBoard()                                                               #draws the board
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#SPECIAL MENU TURTLE 
turtle.addshape("menu.gif")
menu = turtle.Turtle()
menu.shape("menu.gif")
menu.hideturtle()
menu.penup()
menu.goto(50, 0)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ADDING SHAPES TO THE MODULE 
turtle.addshape("bull.gif")
turtle.addshape("cow.gif")
turtle.addshape("ladder.gif")
turtle.addshape("ladder2.gif")
turtle.addshape("ladder3.gif")
turtle.addshape("snake.gif")
turtle.addshape("snake2.gif")
turtle.addshape("snake3.gif")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#DEFINING TURTLES 
ladder = turtle.Turtle()
ladder.shape("ladder.gif")
ladder2 = turtle.Turtle()
ladder2.shape("ladder2.gif")
ladder3 = turtle.Turtle()
ladder3.shape("ladder3.gif")
snake = turtle.Turtle()
snake.shape("snake.gif")
snake2 = turtle.Turtle()
snake2.shape("snake2.gif")
snake3 = turtle.Turtle()
snake3.shape("snake3.gif")
bull = turtle.Turtle()                                                          #bull and cow added last so they are infront of ladders/snakes
bull.shape("bull.gif")
cow = turtle.Turtle()
cow.shape("cow.gif") 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ALL BOARD TURTLES 
allShapes = [cow, bull, ladder, ladder2, ladder3, snake, snake2, snake3]        #Set with all the above turtles in it 
for turt in allShapes:                                                          #loop for all turtles within the set
    turt.penup()                                                                 
    turt.speed(0)                                                               
    turt.hideturtle()                                                           #hides all turtles so you cant see them move along the board 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#PLAYER START POSITIONS(SEPERATED)                                              #placed above shape start positions as they rely on this for cords 
bull.goto(-230, -320)                                                           #bull: x = +70 , y = +30 // cow: x = +70 , y = +80 :from start corner of board
cow.goto(-230, -270)                                                            #used above comment to place exact values of snakes/ladders
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#START POSITIONS OF ALL BOARD SHAPES
#the maths used below allows me to have specific cords and to set cords easier rather than guessing points on the board // allows all objects to be evenly placed upon board 
ladder.goto(bull.xcor()+140, bull.ycor()+2*140-30)                              #all maths for cords done in multiples of 140(1 board square)/+70(bull start x)/+30(bull start y)
ladder2.goto(bull.xcor()+2*140, bull.ycor()+4*140-30)                       
ladder3.goto(bull.xcor()+4*140, bull.ycor()+140+30)
snake.goto(bull.xcor()+3*140, bull.ycor()+4*140-140/2-30)                       #140/2: because snake traverses 3 squares. didnt write 70 to ensure maths follows rules
snake2.goto(bull.xcor()+2*140, bull.ycor()+140/2+30)
snake3.goto(bull.xcor(), bull.ycor()+140+140/2+30)                              
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ALL BOARD TURTLES REVEAL THEMSELVES IN POSITION
for turt in allShapes:                                  
    turt.showturtle()                                                           #reveals all turtles in their correct positions 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#SPECIAL DICE TURTLE                                                            #can assign image to turtle as needed later on
dice = turtle.Turtle()                                                          #will use dice.showturtle when dice is rolled
dice.hideturtle()                                                               #hiding dice turtle, unhide when needed
dice.penup()                                                                    #penup whilst turtle moves to screen position 
dice.goto(500, 0)                                                               #dice position on screen                                                   
turtle.addshape("dice1.gif")                                                    #imports all dice images to this file
turtle.addshape("dice2.gif")
turtle.addshape("dice3.gif")
turtle.addshape("dice4.gif")
turtle.addshape("dice5.gif")
turtle.addshape("dice6.gif")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#SPECIAL WIN TURTLE
win = turtle.Turtle()
win.hideturtle()
turtle.addshape("win.gif")
win.shape("win.gif")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#SPECIAL GOODBYE TURTLE
Goodbye = turtle.Turtle()
Goodbye.hideturtle()
Goodbye.penup()
Goodbye.goto(210,0) #Moves Turtle to be seen with full text when console open
turtle.addshape("thank_you_for_playing.gif")
Goodbye.shape("thank_you_for_playing.gif")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL VARIABLES
p1 = input("Player 1(Cow): Please enter name: \n") 
p2 = input("Player 2(Bull): Please enter name: \n")
squareBull = 1
squareCow = 1
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#PLAYER SPEED SETTINGS
while True:                                                                     
    spd = input("PLAYER SPEED: Enter a value between 1 and 10:\n1 = Slow and 10 = Fast\n")
    if spd != '1' and spd != '2' and spd != '3' and spd != '4' and spd != '5' and spd != '6' and spd != '7' and spd != '8' and spd != '9' and spd != '10':
        print("Incorrect Value.\n")
    else:
        spd.isdigit()                                                           #converts string number into an integer 
        cow.speed(int(spd))                                                     #changes the player speed based upon their input 
        bull.speed(int(spd))
        break
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#DICE ROLL FUNCTION
def DiceRollBull():
    global p2
    roll = random.randint(1,6)                                                  
    input("\nPRESS ENTER TO ROLL DICE")                               
    print(p2, "rolled a", roll)

    if roll ==  1 or 2 or 3 or 4 or 5 or 6:
        dice.shape(f"dice{roll}.gif")                                           #shows the correct dice image according to roll value 
        dice.showturtle()

    global squareBull
    for i in range(roll):                                                       #keeps track of board spaces and directs character movements 
        bull.forward(140)
        squareBull = squareBull + 1
        if squareBull == 25:                                                    #stops character going off board 
            break 
 
        #BOARD EDGES                                                            #special movements for specific board squares (edge peices/snakes/ladders)
        if squareBull == 5 or \
           squareBull == 6 or \
           squareBull == 15 or \
           squareBull == 16:
            bull.left(90)
        elif squareBull == 10 or \
             squareBull == 11 or \
             squareBull == 20 or \
             squareBull == 21:
            bull.right(90)

    #LADDERS                                                                    #MATHS BELOW FOLLOWS RULES OF THE BOARD DRAWING MODULE
    if squareBull == 5:
        print("UP YOU GO!")
        bull.forward(280)
        squareBull = squareBull + 10
    if squareBull == 9:
        print("LUCKY YOU! UP THE LADDER!")
        bull.right(180)
        bull.goto(bull.xcor(),bull.ycor()+140)
        squareBull = squareBull +3
    if squareBull == 18:
        print("CLIMB! CLIMB! CLIMB!")
        bull.right(180)
        bull.goto(bull.xcor(),bull.ycor()+140)
        squareBull = squareBull + 5

    #SNAKES
    if squareBull == 8:
        print("OH NO! Back to the first row!")
        bull.right(180)
        bull.goto(bull.xcor(),bull.ycor()-140)
        squareBull = squareBull - 5
    if squareBull == 20:
        print("Start again! Down, down, down!")
        bull.right(90)
        bull.goto(bull.xcor(),bull.ycor()-140*3)
        squareBull = squareBull -19
    if squareBull == 24:
        print("So close! Down you go")
        bull.goto(bull.xcor(),bull.ycor()-140*2)
        squareBull = squareBull - 10

    #WINNER                                                                     
    if squareBull == 25: 
        print(p2, "you win! Congratulations!")

    #PLAYER POSITION 
    if squareBull < 25:
        print(p2, "is on square", squareBull)                                       

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                #THE 3 FUNCTIONS BELOW ARE THE SAME AS ABOVE WITH MINOR TWEAKS, HENCE NO COMMENTS
def HardDiceRollBull():
    global p2
    roll = random.randint(1,6)                                                  
    input("\nPRESS ENTER TO ROLL DICE")                               
    print(p2, "rolled a", roll)

    if roll ==  1 or 2 or 3 or 4 or 5 or 6:
        dice.shape(f"dice{roll}.gif")                                           
        dice.showturtle()

    global squareBull
    for i in range(roll):                                                        
        bull.forward(140)
        squareBull = squareBull + 1
        if squareBull == 25:                                                    
            break 
 
        #BOARD EDGES                                                           
        if squareBull == 5 or \
           squareBull == 6 or \
           squareBull == 15 or \
           squareBull == 16:
            bull.left(90)
        elif squareBull == 10 or \
             squareBull == 11 or \
             squareBull == 20 or \
             squareBull == 21:
            bull.right(90)

    #LADDERS
    if squareBull == 15: 
        print("DOWN YOU GO!")
        bull.goto(bull.xcor(),bull.ycor()-140*2)
        squareBull = squareBull - 10
    if squareBull == 12: 
        print("UNLUCKY YOU! DOWN THE LADDER!")
        bull.right(180)
        bull.goto(bull.xcor(),bull.ycor()-140)
        squareBull = squareBull -3
    if squareBull == 23: 
        print("FALL! FALL! FALL!")
        bull.right(180)
        bull.goto(bull.xcor(),bull.ycor()-140)
        squareBull = squareBull - 5

    #SNAKES
    if squareBull == 8:
        print("OH NO! Back to the first row!")
        bull.right(180)
        bull.goto(bull.xcor(),bull.ycor()-140)
        squareBull = squareBull - 5
    if squareBull == 20:
        print("Start again! Down, down, down!")
        bull.right(90)
        bull.goto(bull.xcor(),bull.ycor()-140*3)
        squareBull = squareBull -19
    if squareBull == 24:
        print("So close! Down you go")
        bull.goto(bull.xcor(),bull.ycor()-140*2)
        squareBull = squareBull - 10

    #WINNER
    if squareBull == 25: 
        print(p2, "you win! Congratulations!")

    #PLAYER POSITION  
    if squareBull < 25:
        print(p2, "is on square", squareBull)                                       

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def DiceRollCow():
    global p1
    roll = random.randint(1,6)                                                  
    input("\nPRESS ENTER TO ROLL DICE")                                
    print(p1, "rolled a", roll)

    if roll ==  1 or 2 or 3 or 4 or 5 or 6:
        dice.shape(f"dice{roll}.gif")
        dice.showturtle()

    global squareCow
    for i in range(roll):
        cow.forward(140)
        squareCow = squareCow + 1
        if squareCow == 25:                             
            break 

        #BOARD EDGES 
        if squareCow == 5 or \
           squareCow == 6 or \
           squareCow == 15 or \
           squareCow == 16:
            cow.left(90)
        elif squareCow == 10 or \
             squareCow == 11 or \
             squareCow == 20 or \
             squareCow == 21:
            cow.right(90)

    #LADDERS
    if squareCow == 5:
        print("UP YOU GO!")
        cow.forward(280)
        squareCow = squareCow + 10
    if squareCow == 9:
        print("LUCKY YOU! UP THE LADDER!")
        cow.right(180)
        cow.goto(cow.xcor(),cow.ycor()+140)
        squareCow = squareCow +3
    if squareCow == 18:
        print("CLIMB! CLIMB! CLIMB!")
        cow.right(180)
        cow.goto(cow.xcor(),cow.ycor()+140)
        squareCow = squareCow + 5

    #SNAKES
    if squareCow == 8:
        print("OH NO! Back to the first row!")
        cow.right(180)
        cow.goto(cow.xcor(),cow.ycor()-140)
        squareCow = squareCow - 5
    if squareCow == 20:
        print("Start again! Down, down, down!")
        cow.right(90)
        cow.goto(cow.xcor(),cow.ycor()-140*3)
        squareCow = squareCow -19
    if squareCow == 24:
        print("So close! Down you go")
        cow.goto(cow.xcor(),cow.ycor()-140*2)
        squareCow = squareCow - 10

    #WINNER
    if squareCow == 25:
        print(p1, "you win! Congratulations!")

    #PLAYER POSITION
    if squareCow < 25:
        print(p1, "is on square", squareCow)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def HardDiceRollCow():
    global p1
    roll = random.randint(1,6)                                                  
    input("\nPRESS ENTER TO ROLL DICE")                                
    print(p1, "rolled a", roll)

    if roll ==  1 or 2 or 3 or 4 or 5 or 6:
        dice.shape(f"dice{roll}.gif")
        dice.showturtle()

    global squareCow
    for i in range(roll):
        cow.forward(140)
        squareCow = squareCow + 1
        if squareCow == 25:                             
            break 

        #BOARD EDGES 
        if squareCow == 5 or \
           squareCow == 6 or \
           squareCow == 15 or \
           squareCow == 16:
            cow.left(90)
        elif squareCow == 10 or \
             squareCow == 11 or \
             squareCow == 20 or \
             squareCow == 21:
            cow.right(90)

    #LADDERS
    if squareCow == 15:
        print("DOWN YOU GO!")
        cow.goto(cow.xcor(),cow.ycor()-140*2)
        squareCow = squareCow - 10
    if squareCow == 12:
        print("UNLUCKY YOU! DOWN THE LADDER!")
        cow.right(180)
        cow.goto(cow.xcor(),cow.ycor()-140)
        squareCow = squareCow -3
    if squareCow == 23:
        print("FALL! FALL! FALL!")
        cow.right(180)
        cow.goto(cow.xcor(),cow.ycor()-140)
        squareCow = squareCow - 5

    #SNAKES
    if squareCow == 8:
        print("OH NO! Back to the first row!")
        cow.right(180)
        cow.goto(cow.xcor(),cow.ycor()-140)
        squareCow = squareCow - 5
    if squareCow == 20:
        print("Start again! Down, down, down!")
        cow.right(90)
        cow.goto(cow.xcor(),cow.ycor()-140*3)
        squareCow = squareCow -19
    if squareCow == 24:
        print("So close! Down you go")
        cow.goto(cow.xcor(),cow.ycor()-140*2)
        squareCow = squareCow - 10

    #WINNER
    if squareCow == 25:
        print(p1, "you win! Congratulations!")

    #PLAYER POSITION 
    if squareCow < 25:
        print(p1, "is on square", squareCow)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CALLS COW/BULL FUNCTION AND FINISHES GAME 
def game():
    global squareCow
    global squareBull
    global allShapes
    Goodbye.hideturtle()                                                        #removes images after game finishes and restarts 
    menu.hideturtle()
    for turt in allShapes:                                                      #shows board turtles at start of each game 
        turt.showturtle()
    a = [6, 7, 16, 17, 19]                                                      #set a = positions on board in which the characters need to be rotated 180
    b = [10, 15, 20]                                                            #set b = positions on board in which the characters need to be rotated right 90
    
    while True:                                                                 #repeats the game until a player reaches the final square on the board 
        DiceRollCow()                                        
        if squareCow == 25:
            dice.hideturtle()
            win.showturtle()
            time.sleep(2)                                                       #leaves winning message for 2 seconds before executing next code
            for turt in allShapes:                                              #hides all turtles for menu turtle to be seen 
                turt.hideturtle()
            win.hideturtle()
            menu.showturtle()
            break
        DiceRollBull()
        if squareBull == 25:
            dice.hideturtle()
            win.showturtle()
            time.sleep(3)
            for turt in allShapes:
                turt.hideturtle()
            win.hideturtle()
            menu.showturtle()
            break
        
    while True:
        option = input("\nPress 1 to play again, or, 2 to exit:\n")             #option to restart the game 


        while option != '1' and option != '2':                                  #corrects wrong input 
            print("\nINVALID INPUT. PLEASE CHOOSE FROM OPTIONS PROVIDED: 1 or 2:\n")
            option = input()
        if option == '1':                                                       #restarts the game on current mode                            

            menu.hideturtle()                                                   #menu sign dissapears 
            for turt in allShapes:                                              #shows board peices again 
                turt.showturtle()
        
            #Cow resets
            if squareCow in a:                                                  #rotates set a
                cow.left(180)
            elif squareCow in b:                                                #rotates set b
                cow.right(90)

            #Bull resets
            if squareBull in a:
                bull.left(180)
            elif squareBull in b:
                bull.right(90)
            

            #sets up new start

            print("\nNEW GAME---NEW GAME---NEW GAME---NEW GAME\n")
            bull.goto(-230, -320)                                               #start positions                                              
            cow.goto(-230, -270)
            squareCow = 1                                                       #resets the square variables 
            squareBull = 1
            game()                                                              #calls the game function to repeat 

        elif option == '2':
            #Cow resets
            if squareCow in a:                                                  #rotates set a
                cow.left(180)
            elif squareCow in b:                                                #rotates set b
                cow.right(90)

            #Bull resets
            if squareBull in a:
                bull.left(180)
            elif squareBull in b:
                bull.right(90)

            Goodbye.showturtle()
            for turt in allShapes:
                turt.hideturtle()
                
            print("\nThank you for playing! Goodbye!\n\nExiting to main menu...\n")
            dice.hideturtle()
            time.sleep(2)                                                       #delay for real feel video game loading 
            bull.goto(-230, -320)                                               #start positions on peices                                              
            cow.goto(-230, -270)
            Goodbye.hideturtle()
            squareCow = 1                                                       #resets the square variables 
            squareBull = 1
        break

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                #FUNCTION BELOW IS THE SAME AS ABOVE WITH MINOR TWEAK, HENCE NO COMMENTS 
def HardGame():
    global squareCow
    global squareBull
    global allShapes
    Goodbye.hideturtle()                                                        
    menu.hideturtle()
    for turt in allShapes:
        turt.showturtle()
    a = [6, 7, 16, 17, 19]                                                      
    b = [10, 15, 20]                                                            
    
    while True:                                                                 
        HardDiceRollCow()                                        
        if squareCow == 25:
            dice.hideturtle()
            win.showturtle()
            time.sleep(2)
            for turt in allShapes:
                turt.hideturtle()
            win.hideturtle()
            menu.showturtle()
            break
        HardDiceRollBull()
        if squareBull == 25:
            dice.hideturtle()
            win.showturtle()
            time.sleep(3)
            for turt in allShapes:
                turt.hideturtle()
            win.hideturtle()
            menu.showturtle()
            break
        
    while True:
        option = input("\nPress 1 to play again, or, 2 to exit:\n")               


        while option != '1' and option != '2':
            print("\nINVALID INPUT. PLEASE CHOOSE FROM OPTIONS PROVIDED: 1 or 2:\n")
            option = input()
        if option == '1':

            menu.hideturtle()
            for turt in allShapes:
                turt.showturtle()
        
            #Cow resets
            if squareCow in a:                                                      
                cow.left(180)
            elif squareCow in b:                                                    
                cow.right(90)

            #Bull resets
            if squareBull in a:
                bull.left(180)
            elif squareBull in b:
                bull.right(90)
            

            #sets up new start

            print("\nNEW GAME---NEW GAME---NEW GAME---NEW GAME\n")
            bull.goto(-230, -320)                                                                                                
            cow.goto(-230, -270)
            squareCow = 1                                                           
            squareBull = 1
            HardGame()                                                          #calls hard mode function instead of normal mode                                                             

        elif option == '2':
            #Cow resets
            if squareCow in a:                                                      
                cow.left(180)
            elif squareCow in b:                                                    
                cow.right(90)

            #Bull resets
            if squareBull in a:
                bull.left(180)
            elif squareBull in b:
                bull.right(90)

            Goodbye.showturtle()
            for turt in allShapes:
                turt.hideturtle()
                
            print("\nThank you for playing! Goodbye!\n\nExiting to main menu...\n")
            dice.hideturtle()
            time.sleep(2)                                                           
            bull.goto(-230, -320)                                                                                                 
            cow.goto(-230, -270)
            Goodbye.hideturtle()
            squareCow = 1                                                           
            squareBull = 1
        break





       
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
