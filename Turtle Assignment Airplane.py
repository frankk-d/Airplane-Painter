'''
====================================
Turtle Assignment Airplane
Frank Ding
June 19 2022
Python 3.7.9
====================================
Problem Definition: Create a program of an airplane using Turtle graphics

Input: None
Output: image of a concorde airplane with a city background

Process:
    for z in range(7): (repeats the amount of mountains)
        for x in range(4): (draws the height of the mountains)

    for a in range(60): (draws 60 buildings)
        if a == 10: (draws the world trade center at the 10th building)
        if a == 30: (draws the CN Tower at the 30th building)
    for x in range(number): (prints windows)


====================================
List of Identifiers:
    t is equal to turtle.Turtle();

    VARIABLES are located in the FUNCTIONS

====================================
'''
from turtle import *;  # IMPORT turtle
from random import randint;  # IMPORT randint from random
import random;  # IMPORT random
import turtle;  # IMPORT turtle

t = turtle.Turtle();  # REPRESENT 't' as turtle.Turtle();
t.hideturtle();  # hides the turtle

turtle.setup(900, 900);  # makes the document 900 by 900 pixels wide
t.screen.bgcolor("#2A3195");  # sets the background color to #2A3195
t.speed(0);  # sets the turtle speed to 0

t.shape("triangle");  # sets the shape of the turtle to a triangle


# creates the sky
def sky(x, y, color, radius):  # DEFINE 'sky' function with x,y,color, and radius required arguments
    '''
    Function: sky
    Description: prints the sky
    Returns: none
    '''
    t.up();                     #lifts turtle
    t.goto(x, y);               #goes to x,y
    t.fillcolor(color);         #sets the fill color to 'color'
    t.setheading(90);           #sets the heading to 90
    t.begin_fill();             #starts fill
    t.circle(radius, 360);      #draws circle to radius, 360 degrees
    t.end_fill();               #ends fill

#creates RANDOMLY GENERATED MOUNTAINS!
def mountain(x, y, color, heading, maxHeight, space):   #DEFINE 'mountain' function with x,y,color, heading,maxHeight, and space required arguments
    '''
    Function: mountain
    Description: prints the mountains randomly generated
    Parameters:
        x is the x coordinate
        y is the y coordinate
        color is the color
        heading is the angle
        maxHeight is the maximum height for the mountain
        space is the space between the mountains
    Returns: none
    '''
    t.up();                     #lifts turtle
    t.goto(x, y);               #goes to x,y
    t.fillcolor(color);         #fill color set to color
    t.setheading(0);            #sets heading to 0
    for z in range(7):          #LOOP: repeats 7 times increasing by 1
        t.begin_fill();         #begins fill
        for x in range(4):      #LOOP: repeats 4 times increasing by 1
            t.setheading(randint(30, heading));     #sets heading to random integer from 30 to heading
            t.fd(randint(50, maxHeight));           #moves forward randomly (from 50 to the max)
        for x in range(4):                          #LOOP: repeats 4 times increasing by 1
            t.setheading(randint(360 - heading, 360 - 30));     #sets heading to random integer
            t.fd(randint(20, 49));                              #moves forward by a random integer from 20 to 49
        t.goto(t.xcor() + (randint(20, 60)), y);                
        t.goto(t.xcor() - (space), y);
        t.end_fill();           #ends fill
        t.setheading(0);        #sets heading to 0
    t.setheading(270);          #sets heading to 270
    t.fd(500);                  #move forward 500
    t.goto(t.xcor(), y);
    t.goto(x, t.ycor());

#makes a big rectangle
def rectangle(x, y, length, height, color, heading):        #DEFINE 'rectangle' function with x,y,length,height,color,heading required arguments
    '''
    Function: rectangle
    Description: makes a big rectangle
    Parameters:
        x is the x coordinate
        y is the y coordinate
        length is length
        height is height
        color is the color of the rectangle
        heading is the heading of the rectangle
    Returns: none
    '''
    t.up();                 #lifts turtle
    t.fillcolor(color);     #fills with color
    t.goto(x, y);
    t.begin_fill();         #begins the fill
    t.setheading(heading);  #sets heading to heading
    for x in range(2):      #LOOP: loops twice, increasing by 1
        t.fd(length);       #moves by length
        t.right(90);        #turns right 90 degrees
        t.fd(height);       #moves by height
        t.right(90);        #turns right by 90
    t.end_fill();           #ends the fill


def buildings(x, y, tower, color):                          #DEFINE 'buildings' function with x,y,tower,color required arguments
    '''
    Function: buildings
    Description: makes RANDOMLY GENERATED BUILDINGS
    Parameters:
        x is the x coordinate
        y is the y coordinate
        tower is the tower value (cntower or world trade)
        color is the color
    Returns: none
    List of Identifiers:
        topPosition is basically a position of the turtle
        yRandom is random y
        xRandom is randomX
    '''
    t.up();             #lifts turtle
    yValue = y;         #DECLARE yValue equal to y
    topPosition = 0;    #INITIATE: 'topPosition'
    yRandom = 0;        #INITIATE: 'yRandom'
    xRandom = 0;        #INITIATE: 'xRandom'
    t.goto(x, y);
    for a in range(60):             #LOOP: loops 60 times increasing 1
        t.pensize(1);               #turtle size 1
        t.pencolor(color);          #pen color to color
        t.down();                   #puts down turtle
        yRandom = random.randint(20, 80);       #DECLARE 'yRandom' equal to random integer from 20 to 80
        xRandom = random.randint(10, 30);       #DECLARE 'xRandom' equal to random from 10 - 30
        t.fillcolor(color);         #fills color
        t.begin_fill();             #begins fill
        t.setheading(90);           #sets heading 90
        t.fd(yRandom);              #forward random
        t.setheading(0);            #sets heading 0
        t.fd(xRandom);              #forward random
        t.setheading(270);          #sets heading 270
        t.fd(yRandom);              #forward random
        t.end_fill();               #ends fill
        if a == 10:                 #SELECT: if 'a' is equal to 10
            # one world trade
            t.pencolor("#3b3433");          #sets pen color
            t.fillcolor("#290328")          #sets fill color
            t.begin_fill();                 #begins the fill
            t.setheading(88);       #sets heading
            t.fd(180);              #forward 180
            t.setheading(0);        #sets heading to 0
            t.fd(15);               #forward 15

            t.pensize(2);           #sets pensize to 2
            t.pencolor("black");    #pen color is black
            t.setheading(90);       #sets heading to 90
            t.fd(50);               #moves forward 50
            t.setheading(270);      #sets heading 270
            t.fd(50);               #moves forward 50
            t.pencolor("#3b3433");  #sets pen color 
            
            t.pensize(1);           #pensize is 1
            t.setheading(0);        #sets heading 0
            t.fd(15);               #forward 15
            t.setheading(272);      #sets heading 272
            t.fd(180);              #forward 180
            t.end_fill();           #ends the fill
            t.setheading(92);       #sets heading 92
            t.fd(180);              #forward 180
            t.setheading(270);      #sets heading 270

            t.right(5);             #tilt right
            t.fd(180);          #forward 180
            t.right(180);       #right 180
            t.fd(180);          #forward 180
            t.setheading(180);      #heading 180
            t.fd(30);           #forward 30
            t.setheading(270);      #heading 270
            t.left(5);          #left 5
            t.fd(180);          #forward 180
            t.left(180);        #moves left 180
            t.fd(180);          #moves forward 180

            t.setheading(0);    #sets heading to 0
            t.fd(30);           #forward 30
            t.setheading(272);  #heading is 272
            t.fd(180);          #moves forward 180
            t.setheading(180);  #sets heading to 180
            t.fd(45);           #forward by 45

        if a == 30:             #SELECT: if 'a' is equal to 30
            height = 230;       #DECLARE: height is equal to 270
            # cn tower
            t.down();           #puts down turtle
            t.fillcolor("#290328")      #sets color fill
            t.begin_fill();             #begins fill
            t.setheading(88);       #heading is 88
            t.fd(height);           #moves forward by height
            topPosition = t.pos();  #DECLARE: 'topPosition' is equal to position of turtle
            t.setheading(0);        #heading is 0
            t.fd(15);               #forward by 15
            t.setheading(272);      #heading 272
            t.fd(height);           #forward height
            t.end_fill();           #ends the fill

            t.up();                 #lifts the turtle
            t.goto(topPosition);    #goes to 'topPosition'
            t.setheading(180);      #sets the heading to 180
            t.down();               #puts turtle down
            t.begin_fill();         #begins the fill
            t.fd(5);                #forward by 5
            t.circle(-10, 90);      #makes a circle
            t.fd(5);                #forward by 5
            t.circle(-10, 90);      #makes a circle
            topPosition = t.pos();  #DECLARE: 'topPosition' is equal to position of turtle
            t.fd(25);               #moves forward
            t.circle(-10, 90);      #circle
            t.fd(5);                #forward by 5
            t.circle(-10, 90);      #circle created
            t.fd(5);                #forward by 5
            t.end_fill();           #ends the fill
        
            topPosition1 = t.pos(); #DECLARE: 'topPosition1' is equal to the position of the turtle
        
            def beam(color, minus):         #DEFINE 'beam; function with color and minus required arguments
                '''
                Function: beam
                Description: makes the beam of the cn tower
                Parameters:
                    color is the color
                    minus is the amount subtracted from the length of the beam
                '''    
                t.up();                     #lifts turtle
                t.goto(topPosition1);       
                t.fillcolor(color);         #fills color
                t.setheading(180);          #heading 180
                t.fd(5);                     #forward 5
                t.setheading(270);          #heading 270
                t.begin_fill();             #starts fill
                t.fd(height - minus);       #forward
                t.right(90);                #tilts right 90
                t.fd(5);                    #forward by 5
                t.right(90);                #rotate right 90
                t.fd(height - minus);       #forward
                t.end_fill();               #ends the fill

            beam("#7E28E0", 0);             #CALL 'beam' function with the color and the amount to subtract from the height as arguments (same thing for the bottom)
            beam("#3E159E", 50);
            beam("#560561", 100);
            beam("#4D0026", 150);

            # top
            t.fillcolor("#290328")          #fills color
            t.up();                         #lifts turtle
            t.goto(topPosition);        #goes to 'topPosition'
            t.setheading(0);            #sets heading to 0
            t.fd(8);                #forward 8
            t.down();               #down turtle
            t.begin_fill();         #begins the fill
            t.setheading(90);       #sets the heading 90
            t.fd(50)                #foward 50
            t.setheading(0);        #heading 50
            topPosition = t.pos();  #DECLARE: topPositon is equal to position of turtle
            t.fd(9);                #forward 9
            t.setheading(270);      #sets heading 270
            t.fd(50);               #forward 50
            t.end_fill();           #ends the fill
        
            t.up();                 #lifts the turtle
            t.fillcolor("#C20A7B")  #fills the color
            t.goto(topPosition);    #goes to 'topPosition'
            t.setheading(0);        #sets heading 0
            t.fd(3);                #forward 3
            t.down();               #down turtle
            t.begin_fill();         #begins turtle fill
            t.setheading(90);       #sets heading to 90
            t.fd(30);               #forward by 30
            t.setheading(0);        #heading is 0
            topPosition = t.pos();  #DECLARE: 'topPosition' is equal to position of turtle
            t.fd(3);                #forward 3
            t.setheading(270);      #heading 270
            t.fd(30);               #moves forward
            t.end_fill();           #ends the fill

            t.up();                 #lifts turtle
            t.goto(topPosition);
            t.setheading(0);        #sets heading
            t.fd(2);                #moves forward
            t.setheading(90);       #sets heading to 90
            t.down();               #down turtle
            t.pensize(2);           #pensize is equal to 2
            t.fd(30);               #forward by 30

            t.pensize(1);           #pensize decreased to 1
            t.up();                 #lifts turtle
            t.setheading(270);      #heading 270
            t.fd(300);              #forward 300
            t.setheading(180);      #heading 180
            t.fd(100);              #forward 100
            t.goto(t.xcor(), yValue);       


def planeBody(x, y, color):     #DEFINE 'planeBody' function with x,y,color required arguments
    '''
    Function: planeBody
    Description: makes the plane body
    Parameters:
        x is the x coordinate
        y is the y coordinate
        color is the color
    Returns: none
    '''
    t.up();                     #lifts turtle
    t.goto(x, y);       
    t.down();           #down turtle
    t.fillcolor(color); #fills color to color
    t.begin_fill();     #begins fill
    t.setheading(20);   #sets heading to 20
    t.fd(400);          #forward 
    t.circle(-40, 15);      #makes a circle 15 %
    t.fd(80);           #forward 80
    t.left(165);  # heading is 170
    t.fd(60);       #forward
    t.right(10);  # heading is 160
    t.fd(25);       #forward turtle
    t.circle(30, 40);       #makes a circle 40%
    t.fd(475);      #moves forward 475
    t.goto(x, y);   
    t.end_fill();   #ends the fill


def planeFin(x, y):         #DEFINE 'planeFin; function with x,y required arguments]
    '''
    Function: planeFin
    Description: makes the plane fin
    Parameters:
        x is the x coordinate
        y is the y coordinate
    '''
    t.up();                 #lifts turtle
    t.goto(x, y);           
    t.fillcolor("#e83345"); #sets fill color
    t.begin_fill();         #begins the fill
    t.down();               #puts turtle down
    t.setheading(185);      #sets heading 185
    t.fd(50);               #forward 50
    t.circle(-40, 25)  # heading is 160
    t.fd(35);               #forward 35
    t.circle(5, 40);        #circle 40%
    t.fd(35);               #forward 35
    t.setheading(275);      #sets heading 275
    t.fd(50);               #forward 50
    t.end_fill();           #ends fill
    t.left(180);        #rotates 180
    t.fd(50);           #moves forward
    t.setheading(290);  #sets heading
    t.fd(50);           #moves forward


def windows(x, y, number):          #DEFINE 'windows' function with x,y,number required arguments
    '''
    Function: windows
    Description: makes the windows of the concorde
    Parameters:
        x is the x coordinate
        y is the y coordinate
        number is the number of windows
    '''
    t.up();             #lifts turtle
    t.goto(x, y);       #goes to x,y
    t.setheading(20);               #sets heading 20
    for x in range(number):         #LOOP: repeats number amount of times, increasing 1
        t.down();                   #down turtle
        t.dot(3.5);                 #makes a dot
        t.up();                     #lifts
        t.fd(8);                    #moves forward by 8


def door(x, y):         #DEFINE 'door' function with x,y required arguments
    '''
    Function: door
    Description: makes a door :/
    Parameters:
        x is the x coordinate
        y is the y coordinate
    '''    
    t.up();             #lifts turtle
    t.goto(x, y);       
    t.down();           #puts turtle down
    t.setheading(20);   #sets heading to 20
    t.fd(3);            #forward 3
    t.circle(4, 90);    #makes a circle, 90
    t.fd(8);            #forward 8
    t.circle(4, 90);    #circle 90
    t.fd(3);            #forward 3
    t.circle(4, 90);    #circle 90
    t.fd(8);            #forward 8
    t.circle(4, 90);    #circle 90


def rightWing(x, y, color):     #DEFINE 'rightWing' function with x,y,color required arguments
    '''
    Function: rightWing
    Description: makes the rightWing (surprising I know :P)
    Parameters:
        x is the x coordinate
        y is the y coordinate
        color is the color
    '''    
    t.fillcolor(color);         #fills color
    t.up();             #lifts the turtle
    t.goto(x, y);
    t.down();           #puts down turtle
    t.begin_fill();     #starts the fill
    t.setheading(200);  #sets the heading 200
    t.left(15);         #left 15
    t.fd(80);           #forward 80
    t.circle(30, 60);   #circle 60 dergrees
    t.fd(10);           #forward by 10
    t.circle(-30, 60);  #makes a circle 60 degrees
    t.setheading(200);  #sets the heading to 200
    t.fd(30);           #forward 30
    t.setheading(170);  #sets heading to 170
    t.fd(145);          #forward 145
    t.setheading(20);   #sets heading to 20
    t.fd(285);          #forward 285
    t.end_fill();       #ends the fill


def leftWing(x, y, color):      #DEFINE 'leftWing' function with x,y,color required arguments
    '''
    Function: leftWing
    Description: makes the left wing
    Parameters:
        x is the x coordinate
        y is the y coordinate
        color is the color of the wing
    '''    
    t.up();             #lifts the turtle
    t.goto(x, y);       
    t.fillcolor(color)  #fills color to color
    t.down();           #down turtle
    t.begin_fill();     #begins the fill
    t.setheading(200);  #sets heading to 200
    t.right(5);         #right 5 degrees
    t.fd(130);          #forward 180 
    t.circle(-100, 10); #circle 10 degrees
    t.fd(80);           #forward 80
    t.circle(100, 15);  #circle 15 degrees
    t.fd(90);           #forward 90
    t.setheading(350);  #sets heading 350
    t.fd(75);           #forward 75
    t.end_fill();       #ends the fill


def flaps(x, y):            #DEFINE 'flaps' function with x,y required arguments
    '''
    Function: flaps
    Description: makes flaps
    Parameters:
        x is the x coordinate
        y is the y coordinate
    '''    
    t.pensize(1);           #sets the pensize to 1
    t.up();                 #lifts the pen
    t.goto(x, y);           
    t.down();               #decreases the pen
    for x in range(2):      #LOOP: repeats twice
        t.setheading(350);  #sets heading
        t.fd(30);           #forward 30
        t.setheading(200);  #sets heading
        t.fd(28);           #forward 28
        t.left(180);        #left 180 degrees
        t.fd(28);           #forward 28

    # engine part
    t.fillcolor("#26010f"); #fill color to that
    t.begin_fill();         #begins fill
    t.setheading(200);      #sets heading to 200
    t.fd(28);               #forward 28
    t.setheading(350);      #sets heading 350
    t.fd(40);               #forward 40
    t.setheading(20);       #heading 20
    t.fd(30);               #forward 30     
    t.setheading(170);      #sets heading 170
    t.fd(40);               #forward 40
    t.end_fill();           #ends the fill

    t.setheading(350);      #sets the heading to 350
    t.fd(40);               #forward by 40

    # last flap
    t.setheading(350);      #sets heading to 350
    t.fd(30);               #forward 30
    t.setheading(200);      #heading is 200
    t.fd(28);               #forward 28
    t.left(180);            #tilts left
    t.fd(28);               #forward
    t.setheading(350);      #sets heading
    t.fd(15);               #forward 15


def engine(x, y):           #DEFINE 'engine' function with x and y required arguments
    '''
    Function: engine
    Description: makes the engine
    Parameters:
        x is the x coordinate
        y is the y coordinate
    '''         
    t.up();                 #lifts the turtle
    t.goto(x, y);
    t.setheading(350);      #sets heading to 350
    t.fd(60);               #forward 60
    t.setheading(200);      #sets heading to 200
    t.fd(29);               #forward 29
    t.down();               #goes down
    for x in range(2):      #LOOP: loops twice, increasing by 1
        t.down();           #goes down
        t.fillcolor("#360003");     #fills color
        t.begin_fill();         #begins the fill
        t.setheading(280);      #sets heading to 280
        t.fd(15);               #forward 15
        t.setheading(350);      #sets heading 350
        t.fd(20);               #forward
        t.setheading(100);      #heading 100
        t.fd(15);               #forward 15
        t.end_fill();           #ends the fill

    t.right(180);               #tilts right
    t.pencolor("black");        #sets pencolor to black
    t.fillcolor("#26011c");     #fills color is that
    t.begin_fill();             #begins the fill
    t.fd(15);               #forward by 15
    t.setheading(20);       #sets heading to 20
    t.fd(30);               #forward by 30
    t.end_fill();           #ends the fill


def wheel(wheelX, wheelY, color):       #DEFINE 'wheel' function with wheelX, wheelY, and color required arguments
    '''
    Function:wheel 
    Description: makes a WHEEL
    Parameters:
        wheelX is the x coordinate
        wheelY is the y coordinate
        color is the color
    '''    
    t.pencolor(color);          #sets pencolor to color

    t.up();         #lifts turtle
    t.goto(wheelX, wheelY);     
    t.setheading(290);      #sets heading 290
    t.fd(20);               #moves forward by 20
    t.circle(7, 270);       #circle 270 degrees
    t.down();               #down turtle
    t.setheading(110);      #heading 110
    t.fd(15);               #forward 15
    t.up();                 #up

    t.goto(wheelX, wheelY); 
    t.setheading(290);      #heading 290
    t.fd(20);               #forward 20
    t.circle(7, 270);       #circle 270 degrees
    t.setheading(170);      #sets heading to 170
    t.fd(8);                #forward by 8
    t.down();               #down
    t.setheading(300);      #sets heading to 300
    t.fd(15);               #forward by 15
        
    t.goto(wheelX, wheelY);
    t.setheading(290);      #sets heading 290
    t.fd(20);               #forward by 20
    t.circle(7, 270);       #makes a circle 270 degrees
    t.setheading(170);      #sets the heading 170
    t.fd(4);                #forward by 4
    t.down();               #down
    t.setheading(110);      #sets heading 110
    t.fd(15);               #forward by 15

    t.up();                 #lifts turtle
    t.goto(wheelX, wheelY)
    t.setheading(290);      #sets heading 290
    t.fd(20);               #forward 20
    t.circle(7, 80);        #circle 80 degrees
    t.down();               #down turtle
    t.fillcolor("#29171d");     #sets fill color
    t.begin_fill();         #begins the fill
    t.setheading(170);      #sets heading to 170
    t.fd(10);               #forward 10
    t.circle(-7, 160);      #circle 160 degrees
    t.setheading(350);      #heading 350
    t.fd(10);               #forward 10
    t.setheading(170);      #heading 170
    t.circle(7, 160);       #circle 160 degrees
    t.end_fill();           #ends the fill
        
    t.up();                 #lifts the turtle
    t.goto(wheelX, wheelY);
    t.setheading(290);      #sets heading to 290
    t.fd(20);               #forward 20
    t.down();               #down turtle
    t.fillcolor("grey");    #fills color grey
    t.begin_fill();         #starts the fill
    t.circle(7, 360);       #makes a circle
    t.up();                 #lifts turtle
    t.end_fill();           #ends the fill


def icon(x, y):             #DEFINE 'icon' function with x,y required arguments
    '''
    Function: icon
    Description: makes an ICON (I know so descriptive)
    Parameters:
        x is the x coordinate
        y is the y coordinate
    '''    
    t.up();                 #lifts turtle
    t.color("white smoke"); #MAKES THE TURTLE WHITE
    t.goto(x, y)            
    t.setheading(110);      #sets heading 110
    t.stamp();              #makes the turtle jump to make a cute little stamp
    for x in range(4):      #LOOP: repeats four times, up by 1
        t.right(10);        #rotate right by 10
        t.stamp();          #stamps
    t.setheading(20);       #heading 20
    t.fd(17);               #forward 17
    t.setheading(110);      #heading 110
    t.down();               #turtle down
    t.pensize(3);           #pensize is 3
    t.circle(17, 360);      #circle is created
    t.pencolor("black");    #pencolor is black


def windowsPilot(x, y, x2, y2):     #DEFINE 'windowsPilot' function with x,y,x2,y2 required arguments
    '''
    Function: windowsPilot
    Description: makes the pilot windows for the concorde
    Parameters:
        x is the x coordinate
        y is the y coordinate
        x2 is the x coordinate
        y2 is the y coordinate
    '''    
    t.up();                 #lifts turtle
    t.fillcolor("black");   #fills the color to black
    t.pensize(1);           #pensize is 1
    t.goto(x, y);
    t.begin_fill();         #begins the fill
    t.setheading(275);      #sets heading to 275
    t.down();               #down turtle
    t.fd(6);                #forward by 6
    t.setheading(185);      #sets heading to 185
    t.fd(5);                #forward 5
    t.goto(x, y);           
    t.end_fill();           #ends the fill
                
    t.up();                 #lifts turtle
    t.goto(x2, y2);
    t.down();               #puts turtle down
    t.begin_fill();         #starts the fill
    t.setheading(275);      #sets the heading to 275
    t.fd(6);                #forward by 6
    t.setheading(5);        #heading 5
    t.fd(15);               #forward 15
    t.goto(x2, y2);         
    t.end_fill();           #ends the fill


def smoke():                #DEFINE 'smoke' function 
    '''
    Function: smoke
    Description: makes the smoke behind
    Parameters: none
    '''    
    def smokeLine(x, y):        #DEFINE 'smokeLine' function with x,y required arguments
        '''
        Function: smokeLine
        Description: makes the line of smoke
        Parameters:
            x is the x coordinate
            y is the y coordinate
        '''    
        t.up();             #makes turtle go up
        t.goto(x, y);       
        t.setheading(200);  #sets heading to 200
        t.down();           #makes turtle go down
        t.pensize(5);       #pensize is 5
        t.pencolor("white");    #pencolor is white
        t.fd(random.randint(100, 150));         #forward randomly
    
        t.up();             #lifts turtle
        t.fd(random.randint(30, 40))        #forward randomly

        t.down();           #makes turtle go down
        t.fd(random.randint(75, 100));      #forward randomly from 75 to 100

    smokeLine(-195.0, -70.0); #CALL smokeLine function with x and y coordinates as arguments (same for all the below)
    smokeLine(-77.0, -94.0);
    smokeLine(-313.0, -76.0);
    smokeLine(-195.0, -70.0);
    smokeLine(-284.0, -16.0);


def runway(x, y):           #DEFINE 'runway' function with x and y required arguments
    '''
    Function: runway
    Description: makes the runway
    Parameters:
        x is the x coordinate
        y is the y coordinate
    '''    
    t.up();                 #lifts turtle
    t.goto(x, y);
    t.down();               #does not lift turtle
    t.pensize(10);          #pensize is 10
    t.pencolor("#363031");      #pencolor is that
    t.fillcolor("#523c41");     #yeah thats the fill color
    t.begin_fill();             #begins the fill
    t.setheading(10);       #sets heading to 10
    t.fd(1000);             #forward by 1000
    t.right(90);            #right by 90 degrees
    t.fd(700);              #forward 700
    t.setheading(190);      #heading is 190
    t.fd(1000);             #forward by 1000
    t.end_fill();           #ends the fill

    t.up();                 #goes up
    t.goto(x, y);       
    t.left(90);             #moves left 90
    t.fd(200);              #forward 200
    t.setheading(10);       #heading 10
    t.fd(600);              #forward 600
    t.pencolor("white");        #pencolor white
    t.pensize(15);          #pensize 15
    for x in range(7):      #LOOP: repeats 7 times increasing by 1
        t.down();           #down turtle
        t.fd(150);          #forward 150
        t.up();             #up turtle
        t.fd(75);           #forward by 75

    # paint
    t.up();                 #lifts the turtle
    t.goto(-525.0, -261.0);
    t.right(90);            #rotates right 90
    t.fd(50);               #forward 50     
    t.setheading(10);       #sets heading to 10
    t.fd(-100);             #moves backwards 100
    t.pencolor("white");    #pencolor is white
    t.pensize(15);          #pensize is 15
    for x in range(20):     #LOOP: 20 times increasing by 1
        t.down();           #down turtle
        t.setheading(10);   #heading 10
        t.fd(200);          #forward 200
        t.up();             #makes turtle go up
        t.left(180);        #left turtle 180
        t.fd(200);          #forward 200
        t.setheading(350);  #heading 350
        t.fd(100);          #forward 100


def grass(x, y):            #DEFINE 'grass' function with x and y required arguments
    '''
    Function: grass
    Description: makes and touches grass
    Parameters:
        x is the x coordinate
        y is the y coordinate
    '''    
    t.up();                 #lifts the turtle
    t.goto(x, y);           
    
    t.fillcolor("#4D464F");     #fills color as that
    t.begin_fill();         #begins the fill
    t.pensize(10);          #pensize is 10
    t.pencolor("#2E2A2E");  #pencolor is that
    t.down();               #down turtle
    t.setheading(190);      #heading is 190
    t.fd(1000);             #moves forward 1000
    t.setheading(270);      #heading 270
    t.fd(500);              #forward 500
    t.setheading(0);        #heading is 0
    t.fd(1000);             #forward 1000
    t.end_fill();           #ends the fill

    t.up();                 #lifts the turtle
    t.goto(x, y);           
    for x in range(10):     #LOOP: repeats 10 times
        t.setheading(190);  #sets heading 190
        t.down();           #turtle down
        t.fd(150);          #forward 150
        t.left(-240);       #left by -240
        t.fd(60);           #forward by 60
        t.left(180);        #left by 180
        t.fd(60);           #forward by 60


def god():              #DEFINE 'god' function
    '''
    Function: god 
    Description: despite the name, this function creates a giant pikachu attacking the city, which I named god for comedic purposes in order to entertain myself more while creating this program
    Parameters: none
    '''    
    # ears  
    t.up();             #lifts the turtle
    t.goto(-143.0, 287.0);
    t.fillcolor("#FDC101");     #fills the color
    t.begin_fill();         #begins the fill
    t.down();           #downs the turtle
    t.goto(-172.0, 339.0);
    t.goto(-118.0, 308.0);
    t.end_fill();       #ends the fill
            
    t.up();             #lifts the turtle
    t.goto(-173.0, 340.0);
    t.fillcolor("black");       #fill color is black
    t.begin_fill();             #begins the fill
    t.down();                   #downs the ears
    t.goto(-165.0, 325.0);
    t.goto(-163.0, 319.0);
    t.goto(-162.0, 317.0);
    t.goto(-159.0, 312.0);
    t.goto(-154.0, 306.0);
    t.goto(-137.0, 319.0);
    t.goto(-141.0, 323.0);
    t.goto(-145.0, 327.0);
    t.goto(-150.0, 334.0);
    t.goto(-156.0, 338.0);
    t.goto(-158.0, 339.0);
    t.goto(-168.0, 342.0);
    t.goto(-171.0, 339.0);
    t.end_fill();

    #right ears
    t.up();                 #lifts the turtle
    t.goto(-103.0, 307.0);
    t.fillcolor("#FDC101"); #fills the color to a deep yellow
    t.begin_fill();         #begins the fill
    t.down();               #downs the turtle
    t.goto(-103.0, 310.0);
    t.goto(-103.0, 314.0);
    t.goto(-103.0, 323.0);
    t.goto(-100.0, 335.0);
    t.goto(-93.0, 348.0);
    t.goto(-84.0, 355.0);
    t.goto(-80.0, 354.0);
    t.goto(-75.0, 343.0);
    t.goto(-73.0, 329.0);
    t.goto(-72.0, 315.0);
    t.goto(-73.0, 310.0);
    t.goto(-82.0, 299.0);
    t.end_fill();           #ends the fill

    t.up();                 #lifts the turtle
    t.goto(-136.0, 119.0);
    t.fillcolor("#FDC101"); #fills color to a deep yellow
    t.begin_fill();         #begins the fill
    t.down();               #downs the turtle
    t.goto(-198.0, 181.0);
    t.goto(-201.0, 155.0);
    t.goto(-271.0, 208.0);
    t.goto(-270.0, 173.0);
    t.goto(-356.0, 267.0);
    t.goto(-366.0, 226.0);
    t.goto(-260.0, 127.0);
    t.goto(-240.0, 143.0);
    t.goto(-181.0, 93.0);
    t.goto(-171.0, 105.0);
    t.goto(-143.0, 90.0);
    t.end_fill();           #ends the fill

    t.up();                 #lift the turtle
    t.goto(-102.0, 329.0);
    t.fillcolor("black");   #fills the color to black
    t.begin_fill();         #begins the fill
    t.down();               #down
    t.goto(-73.0, 327.0);
    t.goto(-72.0, 329.0);
    t.goto(-71.0, 332.0);
    t.goto(-71.0, 335.0);
    t.goto(-72.0, 341.0);
    t.goto(-73.0, 347.0);
    t.goto(-78.0, 355.0);
    t.goto(-81.0, 357.0);
    t.goto(-85.0, 357.0);
    t.goto(-89.0, 356.0);
    t.goto(-95.0, 353.0);
    t.goto(-98.0, 348.0);
    t.goto(-100.0, 341.0);
    t.goto(-101.0, 335.0);
    t.goto(-101.0, 330.0);
    t.end_fill();           #ends the fill

    #makes the tail
    t.up();                 #lifts the turtle
    t.goto(-206.0, 157.0);
    t.fillcolor("brown");   #color is brown to fill
    t.begin_fill();         #begins the fill
    t.down();               #decreases the turtle
    t.goto(-206.0, 158.0);
    t.goto(-196.0, 105.0);
    t.goto(-180.0, 92.0);
    t.goto(-173.0, 103.0);
    t.goto(-142.0, 91.0);
    t.goto(-143.0, 139.0);
    t.goto(-152.0, 135.0);
    t.goto(-198.0, 181.0);
    t.goto(-206.0, 157.0);
    t.end_fill();           #ends the fill

    t.up();                 #lifts turtle
    t.goto(-89.0, 210.0);
    t.fillcolor("#FDC101"); #fills color to that
    t.begin_fill();         #begins the fill
    t.down();               #down
    t.goto(-70.0, 215.0);
    t.goto(-59.0, 218.0);
    t.goto(-49.0, 222.0);
    t.goto(-25.0, 237.0);
    t.goto(-18.0, 240.0);
    t.goto(-5.0, 251.0);
    t.goto(9.0, 263.0);
    t.goto(24.0, 274.0);
    t.goto(33.0, 285.0);
    t.goto(41.0, 296.0);
    t.goto(46.0, 303.0);
    t.goto(49.0, 312.0);
    t.goto(16.0, 303.0);
    t.goto(25.0, 327.0);
    t.goto(3.0, 308.0);
    t.goto(1.0, 342.0);
    t.goto(-11.0, 319.0);
    t.goto(-14.0, 297.0);
    t.goto(-19.0, 286.0);
    t.goto(-27.0, 274.0);
    t.goto(-33.0, 264.0);
    t.goto(-41.0, 254.0);
    t.goto(-48.0, 248.0);
    t.goto(-60.0, 237.0);
    t.goto(-68.0, 235.0);
    t.goto(-77.0, 235.0);
    t.goto(-85.0, 235.0);
    t.goto(-98.0, 236.0);
    t.goto(-103.0, 240.0);
    t.end_fill();           #ends the fill

    t.up();                 #lifts the turtle
    t.goto(-153.0, 261.0);
    t.down();               #doesnt lift the turtle
    t.setheading(90);       #sets heading to 90
    t.fillcolor("#FDC101"); #fills color is that
    t.begin_fill();         #begins the fill
    t.circle(-50, 150);     #makes a circle 150 degrees
    t.setheading(210);      #heading 210
    t.fd(50);               #forward
    t.setheading(0);        #heading 0
    t.fd(50);               #forward
    t.setheading(270);      #heading 270
    t.circle(-50, 40);      #circle 40 degrees
    t.goto(-64.0, 230.0);
    t.goto(-64.0, 227.0);
    t.goto(-64.0, 225.0);
    t.goto(-64.0, 222.0);
    t.goto(-66.0, 210.0);
    t.goto(-66.0, 204.0);
    t.goto(-66.0, 200.0);
    t.goto(-66.0, 200.0);
    t.goto(-67.0, 185.0);
    t.goto(-68.0, 179.0);
    t.goto(-68.0, 172.0);
    t.goto(-68.0, 168.0);
    t.goto(-68.0, 164.0);
    t.goto(-65.0, 155.0);
    t.goto(-63.0, 147.0);
    t.goto(-63.0, 118.0);
    t.goto(-63.0, 111.0);
    t.goto(-61.0, 99.0);
    t.goto(-58.0, 89.0);
    t.goto(-54.0, 74.0);
    t.goto(-51.0, 62.0);
    t.goto(-49.0, 50.0);
    t.goto(-47.0, 34.0);
    t.goto(-46.0, 21.0);
    t.goto(-43.0, 5.0);
    t.goto(-41.0, -9.0);
    t.goto(-39.0, -21.0);
    t.goto(-61.0, -19.0);
    t.goto(-66.0, -10.0);
    t.goto(-75.0, -0.0);
    t.goto(-80.0, 6.0);
    t.goto(-86.0, 16.0);
    t.goto(-86.0, 27.0);
    t.goto(-89.0, 41.0);
    t.goto(-91.0, 50.0);
    t.goto(-94.0, 61.0);
    t.goto(-96.0, 76.0);
    t.goto(-97.0, 82.0);
    t.goto(-97.0, 90.0);
    t.goto(-104.0, 106.0);
    t.goto(-108.0, 108.0);
    t.goto(-116.0, 97.0);
    t.goto(-120.0, 92.0);
    t.goto(-126.0, 79.0);
    t.goto(-128.0, 66.0);
    t.goto(-133.0, 50.0);
    t.goto(-133.0, 35.0);
    t.goto(-133.0, 20.0);
    t.goto(-133.0, 7.0);
    t.goto(-133.0, 5.0);
    t.goto(-138.0, 7.0);
    t.goto(-139.0, 8.0);
    t.goto(-141.0, 26.0);
    t.goto(-143.0, 38.0);
    t.goto(-146.0, 50.0);
    t.goto(-146.0, 66.0);
    t.goto(-146.0, 80.0);
    t.goto(-146.0, 95.0);
    t.goto(-146.0, 110.0);
    t.goto(-146.0, 120.0);
    t.goto(-150.0, 125.0);
    t.goto(-152.0, 133.0);
    t.goto(-154.0, 142.0);
    t.goto(-156.0, 158.0);
    t.goto(-158.0, 170.0);
    t.goto(-158.0, 184.0);
    t.goto(-158.0, 195.0);
    t.goto(-158.0, 211.0);
    t.goto(-158.0, 227.0);
    t.goto(-155.0, 238.0);
    t.goto(-152.0, 248.0);
    t.goto(-151.0, 256.0);
    t.goto(-153.0, 260.0);
    t.end_fill();           #ends the fill
        
    t.up();                 #up turtle!
    t.goto(-125.0, 181.0);
    t.begin_fill();         #fill turtle    !
    t.down();               #down turtle!
    t.goto(-124.0, 179.0);
    t.goto(-115.0, 167.0);
    t.goto(-104.0, 161.0);
    t.goto(-87.0, 160.0);
    t.goto(-68.0, 160.0);
    t.goto(-48.0, 161.0);
    t.goto(-28.0, 166.0);
    t.goto(1.0, 174.0);
    t.goto(8.0, 178.0);
    t.goto(11.0, 184.0);
    t.goto(-5.0, 183.0);
    t.goto(-14.0, 182.0);
    t.goto(4.0, 190.0);
    t.goto(-16.0, 189.0);
    t.goto(7.0, 204.0);
    t.goto(-20.0, 198.0);
    t.goto(-38.0, 195.0);
    t.goto(-54.0, 191.0);
    t.goto(-66.0, 190.0);
    t.goto(-85.0, 188.0);
    t.goto(-96.0, 188.0);
    t.goto(-113.0, 193.0);
    t.goto(-121.0, 200.0);
    t.end_fill();           #turtle stop filling!

    t.up();             #lifts turtle
    t.goto(-128.0, 267.0);
    t.setheading(0);            #heading is 0
    t.fillcolor("red");         #fills color is red
    t.begin_fill();             #begins the fill
    t.circle(-10, 360);         #makes a circle 
    t.end_fill();               #ends the fill

    t.up();                     #lifts the turtle
    t.goto(-105.0, 288.0);
    t.setheading(0);            #sets the heading to 0
    t.fillcolor("black");       #fills the color to black
    t.begin_fill();             #begins the fill
    t.circle(-10, 360);         #makes a circle 
    t.end_fill();               #ends the fill
    t.up();                     #makes turtle go up
        
    t.goto(-120.0, 297.0);
    t.begin_fill();             #begins the fill
    t.goto(-87.0, 297.0);
    t.goto(-87.0, 295.0);
    t.goto(-125.0, 294.0);
    t.end_fill();               #ends the fill

    t.up();                     #lifts the turtle
    t.goto(-99.0, 261.0);
    t.fillcolor("white");       #fill color is white
    t.down();                   #lowers turtle
    t.begin_fill();             #begins the fill
    t.goto(-88.0, 264.0);
    t.goto(-83.0, 262.0);
    t.goto(-76.0, 270.0);
    t.goto(-72.0, 261.0);
    t.goto(-64.0, 270.0);
    t.goto(-63.0, 260.0);
    t.goto(-56.0, 270.0);
    t.goto(-53.0, 261.0);
    t.goto(-103.0, 260.0);
    t.end_fill();               #ends the fill


def design(x, y, color):            #DEFINE 'design' function with x,y,color arguments
    '''
    Function: design
    Description: makes a cool design on the plane
    '''    
    t.fillcolor(color);         #fills with color
    t.up();                     #lifts turtle
    t.goto(x, y);   
    t.begin_fill();             #starts the fill
    t.setheading(200);          #sets the heading to 200
    t.fd(10);                   #moves forward 10
    t.setheading(240);          #heading is 240
    t.fd(10);                   #forward 10
    t.setheading(20);           #heading is 20
    t.fd(10);                   #forward 10
    t.goto(x, y);               
    t.end_fill();           #ends the fill


def funShadow():                #DEFINE 'funShadow' function
    '''
    Function: funShadow
    Description: makes the planes shadow
    Parameters: none
    '''    
    t.goto(-218.0, -67.0);      
    t.setheading(20);           #heading is 20
    t.down();                   #lowers turtle
    t.pensize(5);               #pensize is 5
    t.pencolor("#80747d");      #sets pencolor
    t.fd(400);                  #forward 400
    t.up();                     #lifts 
    t.pencolor("black");        #pen color is black
    t.pensize(2);               #pensize is 2


def airplane1(x, y):            #DEFINE 'airplane1' function with x and y required arguments
    '''
    Function: airplane1
    Description: makes the smaller airplane in the sky
    Parameters:
        x is the x coordinate
        y is the y coordinate
    '''    
    t.pensize(2);               #sets pensize to 2
    t.pencolor("black")         #pencolor is black  
    t.up();                     #lifts turtle
    t.goto(424.0, 363.0);       
    t.fillcolor("blue")         #fills color blue
    t.begin_fill();             #begins the fill
    t.setheading(60);           #sets heading to 60
    t.down();                   #lowers turtle
    t.fd(30);                   #goes forward by 30
    t.setheading(0);            #sets the heading to 0
    t.fd(15);                   #goes forward by 15
    t.setheading(270);          #sets heading to 270
    t.fd(50);                   #goes forward by 50
    t.end_fill();               #ends the fill

    t.up();                     #lifts turtle
    t.goto(x, y);           
    t.down();                   #down turtle
    t.fillcolor("white smoke"); #fills color is white smoke
    t.begin_fill();             #begins the fill
    t.setheading(180);          #sets the heading to 180
    t.fd(150);                  #forward 150
    t.circle(10, 60);           #circle 60 degrees
    t.setheading(195);          #heading is 195
    t.fd(30);                   #forward 30
    t.setheading(0);            #heading is 0
    t.fd(200);                  #forward 200
    t.end_fill();               #end fill

    # windows
    t.up();                     #lifts turtle
    t.goto(305.0, 359.0);   
    for x in range(20):         #LOOP: repeats 20 times, increasing by 1
        t.dot(4);               #makes a dot
        t.setheading(0);        #sets heading to 0
        t.up();                 #lifts turtle
        t.fd(10)                #moves forward 10
        
    # wing
    t.pensize(5);               #pensize is 5
    t.pencolor("blue")          #pencolor is blue
    t.up();                     #moves up
    t.goto(372.0, 354.0);       
    t.setheading(358);          #sets heading to 358
    t.down();                   #down turtle
    t.fd(70);                   #forward 70


def border():                   #DEFINE 'border' function
    '''
    Function: border
    Description: makes the border when full screened
    Parameters: none
    '''    
    t.up();                     #lifts the turtle
    t.fillcolor("black")        #fill color is black
    t.goto(450.0, 450);
    t.begin_fill();             #begins the fill
    t.goto(953.0, 500.0);
    t.goto(951.0, 500.0);
    t.goto(952.0, -491.0);
    t.goto(-959.0, -490.0);
    t.goto(-958.0, 501.0);
    t.goto(-450, 450);
    t.goto(-450, -450);
    t.goto(450, -450);
    t.goto(450.0, 450);
    t.end_fill();               #ends the fill


def background():               #DEFINE 'background' function
    '''
    Function: background
    Description: makes the BACKGROUND by calling other functions
    Parameters: none
    '''    
    # SKY (PURPLE)
    sky(-519.0, -25.0, "#A93583", -600);        #CALL 'sky' function with the coordiantes, color and radius as arguments (same as below)
    # SKY (RED PURPLE)
    sky(-180, 123.0, "#DA3361", -300);
    sky(-379.0, 88.0, "#DA3361", -300);
    sky(-464.0, -17.0, "#DA3361", -300);
    # SKY (ORANGE)
    sky(-392.0, -187.0, "#F65D4E", -500);
    sky(108.0, 13.0, "#F65D4E", -300);
    # SKY (YELLOW)
    sky(-230.0, -145.0, "#F39943", -400);
    sky(-47.0, -90.0, "#EED73F", -300);
    god();                                      #CALL 'god' function

    mountain(-496.0, -20.0, "#e3857d", 40, 60, 100);        #CALL 'mountain' function with coordinates, color, height arguments(same as below)
    mountain(-581.0, -52.0, "#8a403a", 50, 50, 100);
    mountain(-536.0, -65.0, "#4a140f", 40, 60, 160);

    rectangle(-524.0, -52.0, 1100, 500, "#7198a8", 0);      #CALL 'rectangle' function with the coordinates, length, height, color arguments(same as below)
    rectangle(-526.0, -90.0, 1100, 500, "#486075", 0);
    rectangle(-525.0, -138.0, 1100, 500, "#23324A", 0);

    buildings(-538.0, -56.0, 2, "#140200"); #CALL 'buildings' function with -538.0, -56.0, 2, "#140200" arguments

    grass(442.0, -35.0);                    #CALL 'grass' function with 442.0, -35.0 arguments sent

    runway(-525.0, -261.0);                 #CALL 'runway' function with -525.0, -261.0 arguments sent
    t.pensize(1);           #pensize is 1
    t.pencolor("black");    #pencolor is black

    airplane1(461.0, 363.0);        #CALL 'airplane1' function with 461.0, 363.0 arguments sent


# AIRPLANE
def airplane():         #DEFINE 'airplane' function
    '''
    Function: airplane
    Description: makes the concorde
    Parameters: none
    '''    
    t.pensize(2);           #sets the pensize to 2

    wheel(69.0, 34.0, "white smoke");       #CALL 'wheel' function

    t.pencolor("black");                    #pencolor is black
    leftWing(49.0, 30.0, "white smoke");    #CALL 'leftWing' function to make the left wing

    planeFin(-134.0, -7.0)                  #CALL 'fin' function to create the fin
    planeBody(-218.0, -70.0, "white smoke");    #CALL 'planeBody' function to create the body of the plane

    # fun shadow!
    funShadow();                #CALL: 'funShadow' function for the shadow of the concorde

    # MORE AIRPLANE
    door(-166.0, -46.0);            #CALL: 'door' for the door
    t.up();                         #lifts turtle
    t.fd(185);                      #moves forward 185
    door(t.xcor(), t.ycor());       #CALL: 'door' for the door at the coordinates as arguments
    t.up();                         #lifts turtle
    t.fd(125);                      #moves forward 125
    door(t.xcor(), t.ycor());       #CALL: 'door' for the door at the coordinates as arguments

    windows(-155.0, -30.0, 20);     #CALL 'windows' for it to make windows at those coordinates (twenty windows) and passed as arguments
    t.fd(25);                       #forward by 25
    windows(t.xcor(), t.ycor(), 12);        #CALL 'windows' for it to make windows at those coordinates (twelve windows) and passed as arguments

    rightWing(59.0, 35.0, "white smoke");   #CALL 'rightWing' to make the right wing
    flaps(-175.0, -51.0);                   #CALL: 'flaps' for the flaps with coordinates as arguments
    t.pensize(2);                           #pensize is 2

    engine(-175.0, -51.0);                  #CALL 'engine' function
    icon(-242.0, -22.0);                    #CALL 'icon' function
        
    windowsPilot(163.0, 90.0, 167.0, 91.0);     #CALL 'windowsPilot' function with 163.0, 90.0, 167.0, 91.0 arguments

    smoke();                                #CALL 'smoke' function
    design(-201.0, -37.0, "blue");          #CALL 'design' function with the coordinates and the color
    design(-206.0, -42.0, "red");

    # shadow    
    t.pencolor("black");                    #pencolor is black
    planeBody(-12.0, -327.0, "black");      #CALL 'planeBody' function with coordinates and black color
    leftWing(251.0, -200.0, "black");       #CALL 'leftWing' function with coordinates and black color
    rightWing(281.0, -212.0, "black");      #CALL 'rightWing' function with coordinates and black color

    t.up();                                 #lifts turtle
    t.goto(208.0, 115.0);                   
    t.setheading(20);                       #sets heading to 20
    t.write("zoom", font=("Arial", 12, "normal"));      #writes text
                    
    border();                               #CALL: 'border' function 


def main():                 #DEFINE 'main' function
    '''
    Function: main
    Description: calls functions
    Parameters: none
    '''    
    background();
    airplane();


main();         #CALL 'main' function
t.hideturtle(); #hides the turtle
t.done();
