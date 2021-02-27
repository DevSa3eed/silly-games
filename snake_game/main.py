from turtle import Screen, Turtle
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []
for position in positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)

screen.exitonclick()
