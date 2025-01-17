# print welcome sentences
# asking how many turtles to play
# open new window to create evenly spaced turtle
# set different color for the turtle
# move the turtle random increment of their position
# print the winner turtle color

import turtle
import random
import time

WIDTH , HEIGHT = 500, 500
COLORS = ["red","black","black","orange","blue","yellow","cyan","gray"]

def get_number_of_turtle():
    while(True):
        turtle_count = input("Enter how many turtles you like to race (2-10): ")
        if(turtle_count.isdigit()):
            turtle_count = int(turtle_count)
            if(turtle_count>1 and turtle_count<9):
                return turtle_count
                break
            else:
                print("Invalid! give me between 2 to 8")
        else:
            print("Invalid! enter number between 2 to 8")


def create_turtle(turtle_count):
    turtles = []
    spacex = WIDTH /(turtle_count + 1)
    colors= random.sample(COLORS,turtle_count)
    for i in range(turtle_count):
        racers = turtle.Turtle()
        racers.shape("turtle")
        racers.color(f"{colors[i]}")
        racers.penup()
        racers.left(90)
        racers.setpos(-WIDTH//2 +(i+1)*spacex, -HEIGHT//2 +20)
        turtles.append(racers)
    color = race_turtle(turtles,colors)
    print(f"Color of the Winner turtle : {color}")

def race_turtle(turtles,colors):
    while(True):
        for racer in turtles:
            speed = random.randint(1,15)
            racer.forward(speed)

            x,y = racer.pos()
            if y>= HEIGHT//2 +65:
                return colors[turtles.index(racer)]


print("Welcome to turtle racing 🐢🐢🐢 ")
turtle_count = get_number_of_turtle()
create_turtle(turtle_count)
time.sleep(5)






