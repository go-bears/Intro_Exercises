"""
Copy each problem into it's own .py file
name and save the file
run each file in the terminal. Once the program runs successfuly, 
you can move onto the next problem.
 ex.
    $ python exercise1.py


Goals: debugging code for syntax errors, setting variables, 
writing comments for working code, introduce function 
block format, string formatting problem-solving 
"""

# Problem 1a
#please assign values to the variables' 
my_name = None #use a string
my_height = None # use a float
pet_age = None # use an integer
pet_eyes = None # use a string
pet_hair = None #use a string
pet_name = None #use a string
pet_weight = None # use an integer

#write comment on what's happening with the lines of code. 
#For example, explain what %s does to the output.

#
print "Hi %s, how tall you?" % (my_name)

#
print "I'm %f inches tall." % (my_height)

#
print "My pet's name is %s." % (pet_name)

print "%s is %i years old." % (pet_name, pet_age)

#
print "He's %i pounds heavy." % (pet_weight)
print "Actually that's not too %s." % ("heavy")


#replace the < _ > with the correct code
#add comments on what each line is doing

#
print "My pet has %_ eyes and %_ hair." % (pet_eyes, pet_hair)


# this line is tricky, try to get it exactly right
#
print "If I add %f and %_, I get %_." % (
    my_height, pet_weight, my_height + pet_weight)
#1) what does the "," do? 
#2) what does the "+" do? why?

# Problem 1b -- adding features!
# copy and paste the code above into a new .py file
# replace all the hard coded variables to store values collected from 
# raw_input() or input() and then run the code in terminal


#=========================================================================
#Problem 2

#broken code, Can you spot the errors? please fix it
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
5end = "s"
end6 = "y"
end7 = "B'
end8 = "u"
end9 = "r"
edd10 = "g"
end11 = "e"
end13 = "r"

#fix the code below
# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + en10 + end11 + end12

# what does the â€œ,â€ do to the print output?
#
# what does the "+" do to the print output?
#
# what is the difference between how "+" is used here vs. line 55

new_string = end1 + end2 + end3 + end4 + end5 + end6 + " " + end7 + end8 + end9 + end10 + end11 + end12
#what do you think "print new_string" will output?
print new_string

print new_string[0] # what do you thinking this line  will print?
# why, do you think?
print new_string[1] # what do you thinking this line  will print?
# why, do you think?
print new_string[-1] # what do you thinking this line  will print?
# why, do you think?

#
#=========================================================


# Going off script!!!!!!!!!!!!! 
# Yeah, you want more!
# We got you covered!

#============================================================================
#problem 3

#print string formatting with the format() style
print '''Mary had a little lamb.
	Its fleece was white as {}. 
	And everywhere that {} went.'''.format('...', '...') #replace <...> with string
print "The lamb was sure to go"

print "twinkle {} little {} {}".format() #add missing the string values
print "how i wonder what you %s" % () #add missing the string values

print "." * 10  # what'd that do?



#===========================================================
# Problem 4
#1) Broken code: fix the syntax and other errors in this code, 
#2) comment on what each line of code is doing
#please assign values to the variables' 
my_name = None #use a string
my_height = None # use a float
pet_age = None # use an integer
pet_eyes = None # use a string
pet_hair = None #use a string
pet_name = None #use a string
pet_weight = None # use an integer

def string_formatting():  #defining a function, this line is correct --do not change 
    number = input("what's your favorite integer")
    food = raw_input("what's your favorite food"
    print my_name * pet_ag  #
    print type(my_height)   #
    print bool(pet_eyes     #
    print bool(pet_hair) + boole(pet_name)  #
    print float(pet_weight) # 
    print "i love {}".format(food) * num  #

string_formatting()    #calling / activating a function, this line is correct --do not change 

"""
goals: scaffold function block format, syntax error debugging, commenting,

"""

#===========================================================
# Problem 5
"""
Take it further:
Many student use the command line as a game interface
(ie tic-tac-toe, battleship, hangman)

make a tic-tac-toe board using string characters and format 
#each of the nine squares with an integer in the middle using a 
string formatting technique

expected output:

   1   |  2   |  3   
---------------------
   4   |  5   |  6  
---------------------
    7  |  8   |  9
 
 Take it even further!!!:
 use variables assigned values from raw_input() to format each square's label  
 instead of numbers. adjust the spacing as necessary to keep the tic-tac-toe
 board shape
 
 goals: problem solving, string formatting, introduce projects types, introduce
 raw_input(), variables, multiple line strings
 
"""
#=============================================================================
# extra challenge problem 6
""" copy and paste this code into a new file called ascii.py
    run this working code in the terminal as is:

        $ python ascii.py
    
    1) add comments to explain what each line is doing. it's ok to google! or guess!
    2) experiment playing with values assigned num and my_string and see
       what changes
    3) try creating an original automated ascii art generator. play around! 
        suprise us!
        
goals: operators, string manipulation, introduce/scaffold range(), introduce/scaffold loops
"""
num = 10 # assign an integer value to the variable
my_string = "string"  # assign a string value to the variable

for integer in range(num):  # start a for-loop. What do you think this code does? 
                      #
                      # what do you think range(num) does? it's ok to guess :)
                      #
    print integer # explain this ouput
                    #
    print my_string * integer  #explain this output.
                                #
    print (" " * integer) + (my_string * integer) # explain this output
                                                #
    for letter in my_string: # start a 2nd nested for-loop. what does this 2nd for-loop do?
        print letter # explain this output
                             #
        print letter * integer # explain this output.
                         #
        print ("." * integer) + (letter * integer) + ("." * integer) # explain this output.
                                             # 


