#!/usr/bin/env python3

"""
Rock paper scissors playing bot

Command line interface for interacting with the RPS bot. List of commands:
 - r or rock:     Throw rock
 - p or paper:    Throw paper
 - s or scissors: Throw scissors
 - q or quit:     Quit
"""

from bot import Bot

DEBUG = True
# Number of throws to make randomly before using strategy (default 5)
RANDOM_THROWS = 5

def throwToStr(throw):
    """ Input a throw code and return a string """
    if throw == 0: return "Rock"
    elif throw == 1: return "Paper"
    elif throw == 2: return "Scissors"
    else: return "Undecided"

def parseThrow(throw):
    """ Input a string and return the corresponding throw code """
    if throw in ('r', 'rock'): return 0
    elif throw in ('p', 'paper'): return 1
    elif throw in ('s', 'scissors'): return 2

def beatThrow(throw):
    """ Returns the throw that beats the given throw. """
    if throw == 0: return 1
    if throw == 1: return 2
    if throw == 2: return 0

def main():
    numThrows = 0
    cmd = ''

    print(RANDOM_THROWS, 'throws will be chosen randomly before using strategy.')
    while (cmd != 'q') and (cmd != 'quit'):
        botThrow = -1 # Bot throw is -1 when undecided.
        if numThrows <= RANDOM_THROWS: # Random throw needed
            botThrow = Bot.getRandomThrow()
            if DEBUG: print('\nBot\'s random throw:', end=' ')
        else:
            botThrow = Bot.getThrow()
            if DEBUG: print('\nBot\'s throw:', end=' ')

        if DEBUG: print(throwToStr(botThrow))
        

        cmd = input('\nYour throw: ')

        if cmd in ('q', 'quit'): # Quit
            print('Goodbye')
            exit()

        elif cmd in ('r', 'p', 's', 'rock', 'paper', 'scissors'): # User enters a throw
            numThrows += 1
            humanThrow = parseThrow(cmd)

            print(throwToStr(botThrow))
            
            # Determine the winner
            if humanThrow == botThrow: print('Tie')
            elif humanThrow == beatThrow(botThrow): print('You win!')
            elif beatThrow(humanThrow) == botThrow: print('Bot wins')

            # Add to move history
            Bot.throwHistory.append({'human': humanThrow, 'bot': botThrow})


        else: # Bad command entered
            print('I\'m sorry, I could not understand your command.')

        print('---------------')

# Call main() function if run directly
if __name__ == '__main__': main()

