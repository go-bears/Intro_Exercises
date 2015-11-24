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
import time

bricks = [ " ", "[]", "[__]", "[____]", "[______]" ]



def row1(brick4, mortar): 
    mortar = bricks[0]  #sample code, you should replace it
    brick4 = bricks[4]  #sample code, you can replace it
    row1 = (mortar + brick4 + mortar) * 3 #sample code, you can replace it
    brick2 = bricks[2]
    return row1
    
def row2(mortar, brick2):
    mortar = bricks[0] #sample code, you can replace b/c rows don't align right
    brick2 = bricks[2]
    row2 = (brick2 + mortar ) * 6
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
    print row1(bricks[3], bricks[0])
    time.sleep(1)
    print row2(bricks[0], bricks[2])
    time.sleep(1)
    #call row function with relevant argument(s)
    time.sleep(1)
    #call row function with relevant argument(s)
    time.sleep(1)
    #call row function with relevant argument(s)

    
small_wall()

    

"""
sample output of a wall. Note how the seams between the bricks meet at in the middle of another brick.

[__][__][]
[][__][__]
[__][__][]
[][__][__]
[__][__][]

"""
