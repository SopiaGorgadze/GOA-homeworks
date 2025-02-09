from turtle import *
# PROJECT SBG

width(5)
color("grey")
speed(6)

# making the walls
backward(300)
forward(600)

left(90)
forward(300)
left(90)
forward(600)
left(90)
forward(300)         #end of walls

# making the roof

goto(-300,300)

color("darkgrey")
begin_fill()

left(110)
forward(305)
right(38)
forward(330)        

end_fill()

color("grey")
begin_fill()

right(343)                 #some part of the roof that i dont know the name of
forward(20)              

right(90)
forward(20)

right(89)
forward(640)

right(90)
forward(20)

right(90)
forward(20)

end_fill()
 


begin_fill()

goto(-300,250)
forward(600)
left(90)
forward(30)

end_fill()        #end of roof


#drawing the first pole
 
goto(-250,250)
color("grey")
begin_fill()

left(180)
forward(250)

left(90)
backward(50)

left(90)
forward(250)

end_fill() 

#random ahh parts of the pole N1

color("darkgrey")
begin_fill()

right(90)
backward(5)

right(90)
forward(10)

left(90)
forward(65)

left(90)
forward(10)

end_fill()     #end of pole one(or not)

penup()           #pole 2 lalalalala
goto(-200,250)
pendown()

begin_fill()

left(180)
forward(10)

left(90)
forward(70)

left(90)
forward(10)
 
end_fill()

left(180)
forward(10)

right(90)
forward(60)

             
 
color("grey")
begin_fill()

left(90)                 #making the actual pole
forward(240)

left(90)
forward(50)
 
left(90)
forward(240)

end_fill()           #end of the 2 pole

penup()              #drawing the door
goto(-100,0)
pendown()

color("chocolate4")

begin_fill()

forward(100)
right(90)

forward(200) 
right(90)

forward(100) 
right(90)

forward(200) 
right(90)

end_fill()              #end of door

penup()                 #pole thing 3
goto(140,0)
pendown()

color("grey")
begin_fill()

forward(250)
right(90)

forward(50)
right(90)

forward(250)

end_fill()
 
left(180)
forward(240)

color("darkgrey")                #actual pole3

begin_fill()

right(90)
forward(10)

left(90)
forward(10)

left(90)
forward(70)

left(90)
forward(10)

left(90)
forward(70)

end_fill()                #end of pole3


penup()                   #pole 4
goto(250,0)
pendown()
color("grey")

begin_fill()

left(90)
forward(250)

right(90)
forward(50)

right(90)
forward(250)

end_fill()  #end of pole4

penup()
goto(300,250)
pendown()
color("darkgrey")

begin_fill()

left(90)
forward(10)

right(90)
forward(10)

right(90)
forward(70)

right(90)
forward(10)

right(90)
forward(70)

end_fill()     #end of pole4

color("black")
penup()
goto(320,300)
pendown()

left(180)          #making the roof lininig
forward(639)

right(180)
forward(20)
 
left(20)
forward(305)
right(38)
forward(330)      #end of the roof lining

right(343)
forward(20)

right(90)
forward(20)

right(89)
forward(640)

right(90)
forward(15)      

penup()
goto(-300,280)
pendown()

left(180)
forward(25)

left(90)
forward(600)

left(90)
forward(25) #end of roof lining

penup()
goto(100,0)
pendown()

forward(100)
left(90)

forward(200)
left(90)

forward(100)

penup()
goto(0,0)
pendown()

left(180)
forward(100)     #end of door lining

penup()              #drawing the floor
goto(-300,0)
pendown()
width(3)
color("darkgrey")

begin_fill()

right(90)
backward(50)

right(90)
forward(20)

left(90)
forward(700)

left(90)
forward(20)

left(90)
forward(50)
end_fill()      

left(90)
forward(20)

left(90)
forward(70)

color("grey")

begin_fill()

right(90)
forward(50)

right(90)
forward(740)

right(90)
forward(50)

right(90)
forward(50)

end_fill()               #end of floor

color("black")          #floor lining
backward(50)
forward(737)            #end of floor lining

penup()                 #background
goto(100,220)
pendown()

begin_fill()

color("cadetblue2")
begin_fill()

right(90)
forward(100)

right(90)
forward(220)

right(90)
forward(100)

right(90)
forward(220)
end_fill()        #end of the background



penup()
goto(-100,200)
pendown()

color("blue4")        #writing the letter S
width(5)

right(90)
forward(20)

left(90)
forward(20)

right(90)
forward(20)

right(90)
forward(20)

penup()
goto(-100,200)
pendown()

left(180)
forward(20)                #end of letter S

penup()                    #drawing the letter B
goto(0,160)
pendown()

right(180)
forward(30)

right(90)
forward(40)

right(90)
forward(30)

right(90)
forward(40)

right(180)
forward(20)

left(90)
forward(20)            #end of letter B

penup()                #drawing the letter G
goto(50,200)
pendown()

left(90)
forward(40)

left(90)
forward(30)

left(90)
forward(20)

left(90)
forward(10)

penup()
goto(50,200)
pendown()

left(180)
forward(30)       #end of letter G

penup()               #pole thing N1
goto(-310,0)
pendown()
color("lightgrey")
begin_fill()

left(90)
forward(10)

right(90)
forward(70)

right(90)
forward(10)
end_fill()
goto(-310,0)         #end of pole thingy 2

penup()               #pole thing N2
goto(-200,0)
pendown()

begin_fill() 

left(180)
forward(10)

right(90)
forward(70)

right(90)
forward(10)

right(90)
forward(70)

end_fill()         #end of pole thing 2

penup()            #pole thing 3
goto(130,0)
pendown()

begin_fill()

left(270)
forward(10)

right(90)
forward(70)

right(90)
forward(10)

right(90)
forward(70)

end_fill()           #end of pole thing N3

penup()
goto(310,0)
pendown()

begin_fill()

forward(70)
right(90)

forward(10)
right(90)

forward(70)
right(90)

forward(10)
end_fill()                 #end of pole thing N3

penup()
goto(-200,250)
pendown()
color("darkgrey")

forward(10)
left(90)

forward(70)

exitonclick()