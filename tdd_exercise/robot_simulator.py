"""Write a robot simulator program.

A robot factory's test facility needs a program to verify robot movements.
The program simulates a robot's rotation and movements on a hypothetical grid.

A Robot Class has two attributes, coordinates and bearing, as well as
methods that command the robot to turn left and right; to advance one step, either 
on the X or Y axis; execute a set of directions.

Learning Goals: reading code, testing, tdd, familiarization with unittests patterns, 
implementing Class methods, object inhertiance, conditionals, string parsing, loops
"""

# Constants for robot's bearing orientation
NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270

class Robot(object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        """Initializes the Robot class with default parameters 
        for bearing and x,y coordinates."""

        # % 360 is used so the bearing measurement will remain within 0-360 degrees
        self.bearing = bearing % 360
        self.coordinates = (x,y)

    def turn_right(self):
        """Rotates instaniation of Robot class to the right."""

        self.bearing = (self.bearing + 90)  % 360

    def turn_left(self):
        """Rotates instaniation of Robot class to the left."""

        self.bearing = (self.bearing - 90) % 360

    def advance(self):
        """Advances robot instance one step either in the North, 
        South, East, or West direction"""

        # self.coordinates tuple is "unpacked" into local mutable variables
        # because a tuple is immutable
        x,y = self.coordinates
        pass        


    def simulate(self, directions):
        """Simulates a set of given directions.

        This method takes in a string and executes a series of
        robot movements

        For example, the letter-string "RAALAL" means:
          - Turn right
          - Advance twice
          - Turn left
          - Advance once
          - Turn left yet again
        - Say a robot starts at (7, 3) facing NORTH. Then running this stream
          of instructions should leave it at (9, 4) facing WEST. """

        for move in list(directions):
            pass