#!/usr/bin/env python3

import utils

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #displays "Greetings!"
color = ''    #Currently color equals " "
count = 0      #Currently color equals 0
while (color != 'red'): #While color does not equal red....
    color = input("What is my favorite color? ") #Its displaying what's in the parenthesis
    color = color.lower().strip() #accepts most answers of red and pink
    count = count + 1               # You can also write this as count += 1
    if (color == 'red'): #If color equals red
        print('Correct!') #Its printing "Correct!"
    elif (color == 'pink'): #If color equals pink
        print('Close!') #Its printing "Close!"
    else: #If color does not equal red or pink...
        print('Sorry, try again.') #Its printing "Sorry, try again."
print('You guessed it in {0} tries!'.format(count)) #Displays amount of times it took for user to answer with red