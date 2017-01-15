"""
Brick Wall exercise:

Functions are used to isolate different small specific tasks.
Functions abstract action, grouping several actions as a single object, and then you group those actions to create more  bigger and more advanced objects.


Goal: I've given you "starter functions" of  that create different rows.
use the individual brick functions to create rows of bricks to build a "strong" wall. You have to design your "row" functions so that the seams do not meet. (there's a sample below)

Finally, create a small_wall() function that automatically builds the brick wall so it matches the sample output below. Note the seams of the bricks should not line up to make the strongest wall

small_wall() is the trigger to build the entire wall, all the functions return outputs until the last function call.


Take it further:
make a medium_wall() function and a large_wall() function, making sure to use all the brick sizes.


learning goals: abstraction, chaining functions, return vs. print statements, calling functions, passing values through function parameters and arguments, calling elements from a list, global & local scope

"""
from time import sleep

bricks = [ "[]", "[__]", "[____]", "[______]" ]



def row1(brick_size1, brick_size2):
    brick1 = brick_size1 #example code, you can replace it
    brick2 = brick_size2  #example code, you can replace it
    row1 = (brick2 + brick2 + brick1) #sample code, you can replace it
    return row1

def row2(brick_size1, brick_size2, brick_size3):

    brick1 = brick_size1 #sample code, you should replace b/c rows don't align
    brick2 =  brick_size2 #sample code, you should replace b/c rows don't align
    brick3 = brick_size3 #sample code, you should replace b/c rows don't align
    row2 = brick1  * 6 + brick2 + brick3 #sample code, you should replace b/c rows don't align
    return row2

def row3():
    #do something
    return row3


def row4():
    #do something
    return row4

def row5():
     #do something
    return row5



def small_wall():
    """
    example of output of small wall. Note how the seams between the bricks
    meet at in the middle of another brick.

    [__][__][]
    [][__][__]
    [__][__][]
    [][__][__]
    [__][__][]

    """

    print row1(bricks[0], bricks[1])
    sleep(1)
    print row2(bricks[0], bricks[2], bricks[3])
    sleep(1)
    #call row function with relevant argument(s)
    sleep(1)
    #call row function with relevant argument(s)
    sleep(1)
    #call row function with relevant argument(s)

def large_wall():
    """create a function that builds a large wall"""
    # use the return outputs of the current functions to build a larger wall
    # do not alter the row functions after you complete the small wall
    # the small wall and the large wall should both display in the terminal correctly


def main():
    small_wall()
    large_wall()


if __name__ == '__main__':
    main()
