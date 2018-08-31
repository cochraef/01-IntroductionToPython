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
# TODO: 2.
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
black_turtle.go_to(rg.Point(-200, -200))
black_turtle.pen_down()

# Starting Variables
number_of_sides = 4
rotation = 5
size = 300
osize = 300

for k in range(15):
    black_turtle.draw_regular_polygon(number_of_sides, size)

    black_turtle.pen_up()
    black_turtle.left(45)
    black_turtle.forward(osize/20)
    black_turtle.right(45)
    black_turtle.pen_down()

    black_turtle.right(rotation)
    black_turtle.forward(5*rotation)

    size = size - osize/15

window.close_on_mouse_click()
