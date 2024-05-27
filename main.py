# Author : Shubham Chaurasiya
# it's a representation of 8 states and other states can be done in the same way.


import pandas
from turtle import Turtle, Screen

data = pandas.read_csv('states.csv')
locList = []
stateList = []


def strtotuple(strtupple):
    str = strtupple.strip('(')
    strr = str.strip(')')
    utp = strr.split(',')
    xcord = float(utp[0])
    ycord = float(utp[1])

    return xcord, ycord


for locations in data.location:
    locList.append(tuple(strtotuple(locations)))

for states in data.state:
    stateList.append(states)

print(stateList)

tim = Turtle()
screen = Screen()
tim.penup()
tim.hideturtle()
screen.bgpic('inde16.gif')
stateNum = len(stateList)
while True and stateNum > 0:
    inputText = screen.textinput('State', 'Enter the state').lower()
    if inputText in stateList:
        stateNum -= 1
        indx = stateList.index(inputText)
        loc = locList[indx]

        tim.goto(loc)
        tim.write(inputText)

screen.exitonclick()
