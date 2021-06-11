from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_guess= screen.textinput(title="Make your bet", prompt="Which Turtle Will Win the race? Enter a race")
print(user_guess)
color = ["red", "yellow", "green", "orange", "brown", "pink", "blue"]
y_position= [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-240, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >= 220:
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"you are win ! The {winning_color} turtle is win the race")
            else:
                print(f"you lose! The {winning_color} turtle win is winner")
                is_race_on = False

        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)
screen.exitonclick()


