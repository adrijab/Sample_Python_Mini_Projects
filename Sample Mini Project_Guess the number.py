
#Mini-project description — “Guess the number” game

#One of the simplest two-player games is “Guess the number”. The first player thinks of a secret number in some known range while the second player attempts to guess the number. After each guess, the first player answers either “Higher”, “Lower” or “Correct!” depending on whether the secret number is higher, lower or equal to the guess. In this project, you will build a simple interactive program in Python where the computer will take the role of the first player while you play as the second player.

#When discussing ranges in this mini-project, we will follow the standard Python convention of including the low end of the range and excluding the high end of the range. Mathematically, we will express ranges via the notation [low, high). The square bracket of the left of the range indicates that the corresponding bound should be included. The left parenthesis on the right of the range indicates that corresponding bound should be excluded. For example, the range [0, 3) consists of numbers starting at 0 up to, but not including 3. In other words 0, 1, and 2.

#You will interact with your program using an input field and several buttons. For this project, we will ignore the canvas and print the computer's responses in the console. Building an initial version of your project that prints information in the console is a development strategy that you should use in later projects as well. Focusing on getting the logic of the program correct before trying to make it display the information in some “nice” way on the canvas usually saves lots of time since debugging logic errors in graphical output can be tricky.







import simplegui
import random
import math

secret_number = 100
x = 0
y = 100
n = 7
num_of_guesses = 0

def new_game():
    

    global secret_number
   
    secret_number = random.randint(x, y)
    
    global num_of_guesses
    
    num_of_guesses = 0
    
    print "New game starts with ", "(", x, y ,")"
    print "Total number of remaining guesses is", n

# define event handlers for control panel
def range100():
    global x
    x = 0
    global y
    y = 100
    global n
    n = 7
    new_game()
 
def range1000():
    global x
    x = 0
    global y
    y = 1000
    global n
    n = 10
    new_game()
    
    
def input_guess(guess):
    x = int(guess)
    print "Guess was", x
    global num_of_guesses
    num_of_guesses += 1
    remain_guesses = n - num_of_guesses   
    if x > secret_number:
        print "Higher!", "Total number of remaining guesses is", remain_guesses 
        if remain_guesses == 0:
            print "You lose"
            new_game()
    elif x < secret_number:
        print "Lower!", "Total number of remaining guesses is", remain_guesses
        if remain_guesses == 0:
            print "You lose"
            new_game()
    else:
        print "Correct!", "You win, game ends!"
        new_game()
  
   
frame = simplegui.create_frame("Guess the number", 200, 200)

frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)
             
new_game()

