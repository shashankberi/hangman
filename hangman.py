import sys
import random

from tui_board import *
from words import *

STRIKES = 0
MAX = 6
WORD = random.choice(words)

# -------- Game Logic --------
def show_board(STRIKES):
    '''
    tui board representation
    '''

    if STRIKES == 0:
        print(empty_board)
    elif STRIKES == 1:
        print(head)
    elif STRIKES == 2:
        print(torso)
    elif STRIKES == 3:
        print(right_arm)
    elif STRIKES == 4:
        print(left_arm)
    elif STRIKES == 5:
        print(right_leg)
    elif STRIKES == 6:
        print(left_leg)
    else:
        sys.stderr.write("outside range")

def guess_valid(guess: str, STRIKES: int, board: list):
    '''
    checks if an input guess is valid
    '''
    while True:
        if len(guess) != 1 or not guess.isalpha():
            show_board(STRIKES)
            word_board(guess, board)
            print(''.join(board))
            print("please input a valid guess")
            guess = input("guess a letter: ")
        else:
            return guess

def repeat_guess(guess: str, guesses: list, STRIKES: int, board: list):
    '''
    checks if guess is a repeat
    '''
    while True:
        if guess in guesses:
            show_board(STRIKES)
            word_board(guess, board)
            print(''.join(board))
            print(f"you have already guessed the letter {guess}")
            guess = input("guess a letter: ")
        else:
            guesses.append(guess)
            return guess

def word_board(guess: str, board: list):
    '''
    shows the letters if in the word. correct letters must stay in its position
    every turn
    '''
    global WORD

    for i in range(len(WORD)):
        if guess == WORD[i]:
            board[i] = guess

    return board  

        
# -------- Game Loop --------
def play_game():
    '''
    main game loop
    ''' 
    global STRIKES
    global WORD
    guesses = []
    board = ['_'] * len(WORD)
    # print(WORD)     # DEBUG
    
    try:
        while STRIKES < MAX:
            if not guesses:
                show_board(STRIKES)
                print(''.join(board))

            guess = input("guess a letter: ").lower()
            guess = guess_valid(guess, STRIKES, board)
            guess = repeat_guess(guess, guesses, STRIKES, board)

            if guess not in WORD:
                STRIKES += 1
                show_board(STRIKES)
                word_board(guess, board)
                print(''.join(board))
            else:
                show_board(STRIKES)
                word_board(guess, board)
                print(''.join(board))

            # check win
            if '_' not in board:
                print("Congrats, You Win!")
                break
    except KeyboardInterrupt:
        print("\nThanks for Playing")


    if STRIKES == MAX:
        show_board(STRIKES)
        print("Sorry, You Lost")
        print(f"The word was {WORD}")
        



play_game()