"""Memory, puzzle game of number pairs.
Rosa Hola
Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from tkinter import CENTER
from turtle import *
"""se agrego counter"""
from typing import Counter 
from freegames import path

car = path('car.gif')
rubb = ("python", "c++", "html","css","java","flutter","c","cpp","py","django","db","cs","code","pro","stress","macos","windows","linux","data","science","msft","google","fb","intern","yahoo","linkedin","binary","sort","merge","bigO","$","bug","python","c++","html","css","java","flutter","c","cpp","py","django","db","cs","code","pro","stress","macos","windows","linux","data","science","msft","google","fb","intern","yahoo","linkedin","binary","sort","merge","bigO","$","bug")
tiles = list(rubb)
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
nClicks = 0
pares = 0


def square(x, y):
    """Draw black square with pink outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'pink')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global nClicks
    global pares
    nClicks += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        pares += 1


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align = 'center')

    penup()
    goto(-200,200)
    write(nClicks, font=20)
    if pares == 32:
        goto(-100,200)
        write("Juego Completado", font=20)

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
