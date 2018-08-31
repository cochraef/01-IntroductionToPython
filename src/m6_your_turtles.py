"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Evan Cochrane.
"""
###############################################################################
# 1. DONE
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# 2. DONE
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

black_turtle = rg.SimpleTurtle()
black_turtle.pen = rg.Pen('black', 3)
black_turtle.speed = 10

black_turtle.pen_up()
black_turtle.go_to(rg.Point(-300, 50))
black_turtle.pen_down()

# Starting Variables
number_of_sides = 4
rotation = 5
size = 250
osize = size

for k in range(15):
    black_turtle.draw_regular_polygon(number_of_sides, size)

    black_turtle.pen_up()
    black_turtle.left(45)
    black_turtle.forward(osize/20)
    black_turtle.right(45)

    black_turtle.right(rotation)
    black_turtle.forward(500*rotation/size)
    black_turtle.pen_down()

    size = size - osize/15

red_turtle = rg.SimpleTurtle()
red_turtle.pen = rg.Pen('red', 3)
red_turtle.speed = 10

red_turtle.pen_up()
red_turtle.go_to(rg.Point(-250, -300))
red_turtle.pen_down()

# Starting Variables
number_of_sides = 6
rotation = 4
size = 150
osize = size

for k in range(15):
    red_turtle.draw_regular_polygon(number_of_sides, size)

    red_turtle.pen_up()
    red_turtle.left(45)
    red_turtle.forward(osize/20)
    red_turtle.right(45)

    red_turtle.left(rotation)
    red_turtle.forward(500*rotation/size)
    red_turtle.pen_down()

    size = size - osize/15

window.close_on_mouse_click()

