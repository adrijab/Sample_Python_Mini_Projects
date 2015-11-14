#Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows five choices. Each choice wins against two other choices, loses against two other choices and ties against itself. Much of RPSLS's popularity is that it has been featured in 3 episodes of the TV series "The Big Bang Theory". The Wikipedia entry for RPSLS gives the complete description of the details of the game.

#In our first mini-project, we will build a Python function rpsls(name) that takes as input the string name, which is one of "rock", "paper", "scissors", "lizard", or "Spock". The function then simulates playing a round of Rock-paper-scissors-lizard-Spock by generating its own random choice from these alternatives and then determining the winner using a simple rule that we will next describe.

#While Rock-paper-scissor-lizard-Spock has a set of ten rules that logically determine who wins a round of RPSLS, coding up these rules would require a large number (5x5=25) of if/elif/else clauses in your mini-project code. A simpler method for determining the winner is to assign each of the five choices a number:

#0 — rock
#1 — Spock
#2 — paper
#3 — lizard
#4 — scissors
#In this expanded list, each choice wins against the preceding two choices and loses against the following two choices (if rock and scissors are thought of as being adjacent using modular arithmetic).





# Rock-paper-scissors-lizard-Spock template


import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
         return 1
    elif name == "paper":
         return 2
    elif name == "lizard":
         return 3
    elif name == "scissors":
         return 4
    else:
        print "something is wrong"
        
   


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
         return "Spock"
    elif number == 2:
         return "paper"
    elif number == 3:
         return "lizard"
    elif number == 4:
         return "scissors"
    else:
        print "error message"
    

def rpsls(player_choice):
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange (0, 4)
    Comp_choice = number_to_name(comp_number)
    print "Computer chooses", Comp_choice
    y = (comp_number - player_number) % 5
    if y == 1:
        print "Computer wins!"
    elif y == 2:
         print "Computer wins!"
    elif y == 3:
         print "Player wins!"
    elif y == 4:
            print "Player wins!"
    else:
         print "Player and computer tie!"
    print ("\n")        

    


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

