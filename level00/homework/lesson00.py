from turtle import *
width(6)
color("green")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)                      
#end of square


#drawing a door
begin_fill()
forward(70)
color("green")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)  
end_fill()                
#end of door


#drawing a roof
penup()
goto(200, 200)
pendown()
color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
length = 40
angleRotate = 90
#end of roof


#drawing a first window
penup()
color("brown")
goto(175, 125)
pendown()
begin_fill()
color("brown")
begin_fill
left(210)
forward(length)
left(angleRotate)
forward(length)
left(angleRotate)
forward(length)
left(angleRotate)
forward(length)
left(angleRotate)
end_fill()
#end of first window


#drawing a second window
penup()
goto(70, 125)
pendown()
begin_fill()
color("brown")
forward(length)
left(angleRotate)
forward(length)
left(angleRotate)
forward(length)
left(angleRotate)
forward(length)
left(angleRotate)
fillcolor("brown")
end_fill()
penup()
#THE END






