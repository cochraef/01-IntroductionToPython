
answer = 2 ** 5
print(answer * 100)

###############################################################################
# 1. DONE
#   Read the 2 lines of code ABOVE this _TODO_.  That code:
#     1. Computes 2 raised to the 5th power, yielding the object that is
#          the integer 32.
#     2. Makes the name   answer   refer to that object.
#     3. Looks up the object to which the name   answer  refers (i.e., 32).
#     4. Multiplies that object (32) by 100 (hence computing the object
#          that is the integer 3,200).
#     5. Prints the newly-computed object.  (It prints WITHOUT the comma.)
#
#   Make sure that you understand that those two lines do the above,
#     ** ASKING QUESTIONS AS NEEDED. **
#   Once you completely understand the above, run this module,
#   confirming that it prints 3200.  Then change the above _TODO_ to DONE.
##############################################################################

###############################################################################
# 2. DONE
#   Immediately below this _TODO_, write code that:
#     - Computes 77 plus the cosine of 2.75.
#         HINT: You will need to import the   math  module (library).
#     - Stores that computed value using a name of your own choosing.
#     - Prints the square root of that computed value.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

import math as m

x = m.cos(2.75) + 77
print(m.sqrt(x))

###############################################################################
# 3. DONE
#   Immediately below this _TODO_, write code that computes and prints:
#      the square root of ((41 * 88) + (4 * the cosine of 2))
#   Use as few or as many intermediate names as you feel appropriate.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

print(m.sqrt(41 * 88 + 4 * m.cos(2)))

###############################################################################
# 4. DONE
#   Immediately below this _TODO_,
#   write code that computes the square root of 2 in two ways:
#     - By using the   math.sqrt   function.
#     - By raising 2 to the 0.5 power (using   **   for exponentiation).
#   Print both of the expressions that you write.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

print(' ')
print('Square Root of Two (Two ways):')
print(m.sqrt(2))
print(2 ** 0.5)

###############################################################################
# 5. DONE
#   Every object has a TYPE and a VALUE.  For example,
#   for the object that is computed by  math.sqrt(2):
#      Its TYPE is float  (which is shorthand for "floating point number")
#      Its VALUE is (approximately) 1.4142135623730951.
#
#   The TYPE of an object is important because it determines:
#      -- what the object KNOWS, and
#      -- what the object can DO.
#
#   The   type   function returns the TYPE of its argument.  For example,
#       type(3.14)    returns the CLASS (synonym for TYPE) 'float'
#   and so the code:
#       print(type(3.14))
#   will print     <class 'float'>
#   Try it now!
#   (Just write   print(type(3.14))   below this _TODO_ and run the program.)
#
#   Now go through the BLAH objects listed below.  For each:
#      -- Try to GUESS its TYPE.
#      -- Write code of the form   print(type(BLAH)).
#      -- RUN the code to LEARN its TYPE.

#       "hello" Guess: string
#       'hello' Guess: string
#       "a b c" Guess: string
#       3 + 3 Guess: integer
#       "3" + "3" Guess: string
#       2 ** 100 Guess: integer
#       2.0 ** 100 Guess: float
#       math.sin(8) Guess: float
#       math.sin Guess: function
#       print Guess: function
#       math Guess: library
#       'math' Guess: string
#
# After you have written and run the code to learn the TYPE
# of each of the above, change the above _TODO_ to DONE.
###############################################################################

print(' ')
print(type(3.14))

print(type("hello"))
print(type('hello'))
print(type("a b c"))
print(type(3+3))
print(type("3" + "3"))
print(type(2 ** 100))
print(type(2.0 ** 100))
print(type(m.sin(8)))
print(type(m.sin))
print(type(print))
print(type(m))
print(type('math'))
