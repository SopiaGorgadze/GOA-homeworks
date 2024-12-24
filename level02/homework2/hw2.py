from turtle import*

width(5)
color("grey")
speed(15)


#drawing the castle walls
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(50)
left(90)

forward(100)
right(90)

forward(100)
right(90)

forward(100)
left(90)

forward(50)
left(90)

forward(200)
end_fill()


#drawing one of the rooftops of a castle

penup()
goto((0,200))
pendown()
color("black")
begin_fill()

right(210)
forward(50)

left(240)
forward(50)
end_fill()


#drawing the second rooftop
begin_fill()

penup()
goto(200,200)
pendown()

left(180)
forward(50)

right(240)
forward(50)

end_fill()

#drawing the blocks
color("grey")

penup()
goto(50,100)
pendown()
 

right(150)
forward(20)
 

begin_fill()
right(90)
forward(20)
 
right(90)
forward(20)
end_fill()

left(90)
forward(20)

left(90)
forward(20)

begin_fill()
right(90)
forward(20)

right(90)
forward(20)
end_fill()

left(90)
forward(20)

 
left(90)
forward(20)
 
begin_fill()
right(90)
forward(20)

right(90)
forward(20)
end_fill()
 


#drawing the door
color("black")
begin_fill()
 

penup()
goto( 60, 0)
pendown()

left(90)
forward(75)

left(90)
forward(70)

left(90)
forward(70)

left(90)
forward(70)
end_fill()

#drawing the  stick of the flag
width(7)
color("brown")
penup()
goto( 25 , 245)
pendown()

left(180)
forward(20)

#drawing the flag
color("black")
width(3)

forward(20)
right(90)

forward(40)
right(90)

forward(20)
right(90)

forward(40)

left(180)
forward(20)

color("red")
width(5)

left(90)
forward(20)

color("black")
width(3)

left(90)
forward(20)

left(90)
forward(10)

color("red")
width(5)

left(90)
forward(40)

#drawing the  stick of the flag

width(7)
color("brown")
penup()
goto( 175 , 245)
pendown()

left(90)
forward(20)
#drawing the flag
color("black")
width(3)

forward(20)
right(90)

forward(40)
right(90)

forward(20)
right(90)

forward(40)

left(180)
forward(20)

color("red")
width(5)

left(90)
forward(20)

color("black")
width(3)

left(90)
forward(20)

left(90)
forward(10)

color("red")
width(5)

left(90)
forward(40)





exitonclick()
