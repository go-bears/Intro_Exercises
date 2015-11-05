#broken code homework: fixing variables, running python code

#import python's random model
import random


students = ["drew", "meg", "olivia", "piril", "luisa", " jaya", "monique" , 
"jen", "shanae", "theresa", "kelsey", "brittany", "samantha", "sammy", 
"mandy", "angela", "catherine", "thais", "dori"]

#there aren't enough super powers to go around!! please add 7 more super powers 
#to this list
supers = ["wonder", "bat", "super", "lightening", "flash", "invisible", "aqua",
"cat", "hulk", "freeze", "storm", " ", " ", " ", " ", " ", " ", " ", ]


#Broken code!!! Can you find and fix  the syntax errors?
# write comments on what the code is doing on at # mark

def super_shuffles(list1, list2): #defining function -- this line works
   
    random.shuffle(list1) #use imported random module to shuffle list1
    students -- list1  #
    random.shuffle(list2) #use imported random module to shuffle list1
    supers = list2 #

    secret_identities = [] #set variable to an empty list
    for person in student: # start for loop for students list
        for power in suprs: #start start for loop for supers list
            secret = supers.pop() #pop last list element & save to variable
            identity = students.pop() #pop last list element in students & save to variable
            secret_identity = secret + " " + identity #
            print secretidentity #
            
            secret_identities.append((secret_identity)) #append secret_identy variable to to secret identities list
    
    return secret_identities 
            
#function call -- this code is fine
super_shuffles(students, supers) #the feeding the function students list and supers list

print super_shuffles(students, supers) #what is being printed? how is it different from what line 33 is outputting?


"""
on your own: 
*comment out the students and supers lists
*write two original variables that are each assigned list values
*feed the super_shuffles() function with your new variables with list assignments
*change the variable names within the function so they become meaningful to your
project
*make the function work!
"""

"""
Learning Goals: Debugging syntax error, Comments practice, variable assignment,
forking from repository, downloading and running code in Python, reading and 
adapting legacy code.

scaffolding: functions, for-loops, importing modules, built-in modules, lists, 
function calls,
"""

