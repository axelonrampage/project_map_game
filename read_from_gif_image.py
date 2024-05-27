# this file is made to get the coordinates of the states by clicking on them
# further more states can be added in the states.csv file with this method
# and can be read by the main file directly
from turtle import Screen

screen = Screen()
input_image = 'inde16.gif'


def clicksc(x, y):
    print(x, y)


screen.onscreenclick(clicksc)

screen.bgpic(input_image)

screen.mainloop()
