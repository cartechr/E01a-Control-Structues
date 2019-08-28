#!/usr/bin/env python3

import utils

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #displays "Greetings!"
color = input("What is my favorite color? ")  #Its displaying what's in the parenthesis
if (color == 'Red' or color == 'red'): #Beginning of if else statement. If user's input equals 'Red' or 'red' ....
    print('Correct!') #Its printing "Correct!"
else:#If color does not equal 'Red' ot 'red'
    print('Sorry, try again.') #Its printing "Sorry, try again."