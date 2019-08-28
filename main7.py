#!/usr/bin/env python3

import utils

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #displays "Greetings!"
color = input("What is my favorite color? ") #Its displaying what's in the parenthesis
color = color.lower().strip() #accepts most answers of red and pink
if (color == 'red'): #If color equals red
    print('Correct!') #Its printing "Correct!"
elif (color == 'pink'): #If color equals pink....
    print('Close!') #Its printing "Close!"
else: #If color does not equal red or pink...
    print('Sorry, try again.') #Its printing "Sorry, try again."