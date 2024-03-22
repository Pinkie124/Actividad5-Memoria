"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
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
    global tap_count
    tap_count += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    up()
    goto(180, 180)
    color('black')
    write(f'Taps: {tap_count}', font=('Arial', 16, 'normal'))

    if all(not h for h in hide):
      up()
      goto(-50, 0)
      color('black')
      write('¡Todos los cuadros han sido destapados!', font=('Arial', 16, 'normal'))


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    
    color_dict = {}

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    for count in range(64):
        if not hide[count]:
            continue

        x, y = xy(count)
        mark = state['mark']

        if mark == count:
            color('black')
        else:
            num = tiles[count]

            #
            digit_color = color_dict.get(num, choice(['blue', 'green', 'red', 'yellow', 'orange', 'purple']))
            color_dict[num] = digit_color

            color('black', digit_color)

        up()
        goto(x + 25, y + 20)  
        write(tiles[count], align='center', font=('Arial', 15, 'normal'))

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


 
