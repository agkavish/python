# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

secret_number = 0
range_low = 0
range_high = 100
num_guesses_allowed = 0;
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, num_guesses_allowed
    print "Game starting with range ", range_low ,"-" , range_high

    secret_number = random.randrange(range_low,range_high)
    num_guesses_allowed = math.ceil(math.log(range_high - range_low + 1, 2))
    num_guesses_allowed = int (num_guesses_allowed)
    print "Number of guesses allowed " , num_guesses_allowed



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_low, range_high
    range_low = 0
    range_high = 100
    new_game()
   

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_low, range_high
    range_low = 0
    range_high = 1000
    new_game()
  
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, num_guesses_allowed
    guess_number = int(guess)
    print "Guess was " , guess_number
    
    if (secret_number > guess_number):
        print "Higher"
        num_guesses_allowed = num_guesses_allowed -1
        print "Remaining guesses available ", num_guesses_allowed
    elif (secret_number < guess_number):
        print "Lower"
        num_guesses_allowed = num_guesses_allowed -1
        print "Remaining guesses available ", num_guesses_allowed
    else :
        print "Correct"
        new_game()
        
    if(num_guesses_allowed <= 0):
        print "You have exhausted all chances, starting a new game"
        new_game()
  

    
# create frame
frame = simplegui.create_frame('Guess The Number', 200, 200)

# register event handlers for control elements and start frame
inp = frame.add_input('My Guess', input_guess, 50)
range100_button = frame.add_button('1..100', range100)
range1000_button = frame.add_button('1..1000', range1000)

frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
