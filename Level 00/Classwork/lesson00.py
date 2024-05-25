from turtle import *
speed(30)
width(5)

# kvadrati
color("brown")
begin_fill() # shignit gaferadeba
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill() # gaferadeba dasrulebulia

# karebi
forward(70)
color("gray")
begin_fill()
left(90)
forward(100) # karis simagle
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

# saxuravi
color("saddle brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


exitonclick()