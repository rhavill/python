#!/usr/bin/python

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()
def the_flying_circus():
    if not True and False:    # Start coding here!
        # Don't forget to indent
        # the code inside this block!
        return False
    elif False or False or 1 > 2:
        # Keep going here.
        # You'll want to add the else statement, too!
        return False
    else:
        return True
        
clinic()