#!/usr/bin/env python3

import utils

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #displays "Greetings!"
color = input("What is my favorite color? ") #Its displaying what's in the parenthesis
if (color.lower().strip() == 'red'): #accepts most answers of red. Beginning of if else statement.
    print('Correct!') #Its printing "Correct!"
else: #If color does not equal red...
    print('Sorry, try again.') #Its printing "Sorry, try again."