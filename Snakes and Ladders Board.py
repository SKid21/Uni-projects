#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#IMPORT SECTION
import turtle
import random
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TURTLE SETTINGS                                                        
t0 = turtle.Turtle()                                                     
t1 = turtle.Turtle()                                                    
t2 = turtle.Turtle()                                                    
turtles = [t0, t1, t2]                                                  #turtle list/shorter code for next 2 instructions 
for turt in turtles:
    turt.hideturtle()
    turt.speed(0)
t0.width(7)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#SCREEN SET UP
turtle.title("SNAKES AND LADDERS!")                                     
turtle.setup(1440, 1440, 0, 0)                                          #full screen game 
#turtle.bgcolor("Silver")
turtle.addshape("cover.gif")                                            #adding background wallpaper 
cvr = turtle.Turtle()
cvr.shape("cover.gif")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCTION #1
def GameBoard():                                                        #function to draw the game board/will have vertical coloured lines(to represent climbing up as per game)/colours will be chosen at random 
    colors = ["red", "blue", "yellow", "green", "pink", "purple"]       
    colors2= ["violet", "gold", "orange", "azure", "chocolate", "cyan"] #2 sets to guaruntee the saem colour is not used twice / 2nd color set for vertical lines 
    t0.penup()                                                          
    t0.goto(-300, -350)                                                 #board drawing start position
    t0.pendown()                                                        
    t0.begin_fill()                                                     #makes turtle fill the next drawing
    randColor = random.choices(colors, k = 1)                           #creates the variable for random colors
    t0.fillcolor(randColor[0])                                          #chooses the colour for drawing fill 
    for i in range(4):                                                  #outter edge of board
        t0.forward(700)                                                  
        t0.left(90)                                                     
    t0.end_fill()                                                       #whole board filled 1 colour
    t0.begin_fill()                                                     #starts filling effect for bottom loop
    randColor2 = random.choices(colors2, k = 1)                        
    t0.fillcolor(randColor2[0])                                         
    for i in range(2):                                                  #vertical lines 
        t0.forward(140)                                                 
        t0.left(90)                                                     
        t0.forward(700)
        t0.right(90)
        t0.forward(140)
        t0.right(90)
        t0.forward(700)
        t0.left(90)
    t0.end_fill()                                                       #Stops the fill process in order to keep the fill colours vertical
    t0.penup()                                                          
    t0.goto(-300, -210)                                                 #cords for next drawing point
    t0.pendown()                                                         
    for i in range(4):                                                  #horizontal lines 
        t0.forward(700)                                                 
        t0.penup()                                                      #penup in loop so doesnt draw when moving cords 
        t0.goto(t0.xcor()-700,t0.ycor()+140)                            #sets turtle cords to same xcor each iteration while incrementing y each iteration by 140 to create the board squares
        t0.pendown()                                                    #pendown so loops starts with turtle drawing each iteration 
    Numbers()                                                           
    Text()                                                               
#would do the vertical lines in same code styled loop, however this way is not efficient for implementing the coloured verical lines
#used mathematical constants within my board to calculate exact values for the sizes and locations of squares(the board is 700x700, so therefore each row/collumn is 140 apart(140x5=700)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCTION #2
def Numbers():                                                          #function to add incrementing numerical values to each square on the game board 
    x = 1                                                               #setting x as 1 to be used in the loops for numbering each board square
    t1.penup()                                                           
    t1.goto(-280, -250)                                                 #sets position of first numerical value in square "1"
    for i in range(25):                                                 #loop to print numerical values on the bottom row of squares
        t1.write(x, font=("Ariel", 30))                                 #prints the numerical value 
        t1.forward(140)                                                 
        x = x+1                                                         #increments x by 1 in order to give the next square the correct value
        if i == 4:                                                      #moves turtle to next row for numbering
            t1.left(180)                                                 
            t1.goto(280, -110)
        elif i == 9:
            t1.left(180)
            t1.goto(-280, 30)
        elif i == 14:
            t1.left(180)
            t1.goto(280, 170)
        elif i == 19:
            t1.left(180)
            t1.goto(-280, 310)
#used mathematical constants within my board to calculate exact values for the locations of the numbers. hence why the y axis increments in +140 for above loops if statements. x axis goes to 280 and -280 as its opposite sides of board 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCTION 3
def Text():                                                             #function to create text prompt where there is space for user to place their console 
    t2.penup()
    t2.goto(-715, 320)
    t2.color("white")
    t2.write("Place console under here:", font=("Ariel", 30, "bold", "underline"))


