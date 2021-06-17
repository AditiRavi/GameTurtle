import random
import turtle as t

screen = t.Screen()
screen.title("Welcome to the Turtle Race!")

screen.setup(width=500,height=400)
screen.bgcolor("black")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtle=[]
is_race_on = False

for i in range(0, 6):
    turtle_1 = t.Turtle(shape="turtle")
    turtle_1.penup()
    turtle_1.color(colors[i])
    turtle_1.goto(x=-230, y=y_pos[i])
    all_turtle.append(turtle_1)

turtle_ = t.Turtle()
turtle_.color("white")
turtle_.penup()
turtle_.hideturtle()
turtle_.goto(x=-230, y=100)
style = ('SJSJS GAMING', 22, 'bold')
turtle_.write('T U R T L E  R A C E', font=style, align='left')

f=0
if user_bet:

    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        turtle.pendown()
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color=turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner!")
                f = 1
            else:
                print(f"You've lost! The {wining_color} turtle is the winner!")
            break

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
turtle_.hideturtle()
turtle_2 = t.Turtle()
turtle_2.color("white")
turtle_2.penup()
turtle_2.hideturtle()
turtle_2.goto(x=-80, y=-8)
style = ('SJSJS GAMING', 15, 'bold')

if f == 1:
    turtle_2.write('Y O U  W I N !', font=style, align='left')
else:
    turtle_2.write('Y O U  L O S E!', font=style, align='left')
screen.exitonclick()