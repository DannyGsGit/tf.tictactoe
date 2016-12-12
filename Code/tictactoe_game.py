
#### Tic Tac Toe Game ####
"""
*[C] Represent the board as a 9-dimensional array [1, 9].

* Don't care about the sequence of a game, simply score moves against static boards
    * Illegal moves (no move, place over existing gamepiece) are scored as a "loss" (-1)
    * Normal moves that don't end the game are scored neutrally (0).

*[C] Winning boards are a known quantity. We can use them as masks, multiplied over the 
  game board at the end of a move to identify a game winning move. 
  
*[C] Starting player is randomized with each game.

* Game should provide feedback at the end of the turn:
    * Player N placed X/O at Position M.
    * Move Score = X
    * Game Finished/Not Finished
    
* Player move entered as a digit in range 0-8, mapping to placement on the board.
"""

#~~~~~~~~~~~~~~~~~~~~~~
#### Get libraries ####
#~~~~~~~~~~~~~~~~~~~~~~

import pandas as pd
import numpy as np
import random



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Define Functions and baseline variables ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Evaluate a game board against winning boards
def check_winning_board(new_board, winning_board_templates):
    # Arguments:
    # new_board: A list of length 9 reflecting the current state of the game board. 
    #                Function assumes player positions are flagged with -1 and 1. 0 is empty.
    # winning_board_template: a matrix of the winning board possibilities
    #
    # Returns:
    # A boolean True/False depending on whether a win is found
    
    # Use a dot product to mask the current board with the winning boards.
    mask_boards = np.dot(winning_board_templates, np.transpose(new_board))
    
    # If any mask returns a -3 or 3 (player -1 wins or player 1 wins), return True
    eval_win = any(map(lambda each: each in mask_boards, [-3, 3]))
    
    # Return the result
    return(eval_win);



# Check for an illegal move
def check_illegal_move(current_board, new_move):
    # Arguments:
    # current_board: The board (9-dim list) before the move was made
    # new_move: The new move being made, one-hot format (i.e. 9-dim list)
    #
    # Returns:
    # boolean True if illegal move is present, False if the move is legal
    
    # Mask the board and the move. If the move overlays a current piece, 
    # we will get a -1 or 1. Legal moves == 0.
    overlap_move = np.dot(current_board, np.transpose(new_move))
    
    # Check for a non-move. 0 means no move was made.
    did_you_move = sum(new_move)
    
    # Prepare the result
    if (overlap_move != 0 or did_you_move == 0):
        illegal = True
    else:
        illegal = False
    
    # Return result
    return(illegal);



# Display the board in readable format
def display_board(current_board):
    display_format = np.reshape(current_board, (3, 3))
    return(display_format);



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Initialize the game ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Initialize the game with an empty board
game_board = np.array([0] * 9)



# Define winning game boards
winning_boards = np.matrix([[1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 1, 1, 1],
                            [1, 0, 0, 1, 0, 0, 1, 0, 0],
                            [0, 1, 0, 0, 1, 0, 0, 1, 0],
                            [0, 0, 1, 0, 0, 1, 0, 0, 1],
                            [1, 0, 0, 0, 1, 0, 0, 0, 1],
                            [0, 0, 1, 0, 1, 0, 1, 0, 0]])




# Randomly select a player to start
players = np.array([-1, 1])
current_player = random.choice(players)



# Game in progress flag
continue_game = True





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Run through the game ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while continue_game == True:
    ## Make the move
    # Display the board to the player
    print("\n", "\n", "\n", "Your turn Player ", current_player)
    print("Current Board:", "\n", display_board(game_board))
    print("Choose Position:", "\n", display_board(list(range(0,9))))
    
    # Get input from player
    position = input("Enter Position (0-8): ")
    
    
    ## Process the move
    # One-hot encode the move, and validate the input
    entered_move = np.array([0] * 9)
    try:
        position = int(position)
        if (position >= 0 and position <= 8):
            entered_move[position] = current_player
    except ValueError:
        print("You didn't input a valid number")
        
    # Generate new board
    new_game_board = game_board + entered_move
    
    
    ## Run through evaluations
    # Evaluate illegal move
    illegal_move = check_illegal_move(current_board = game_board, new_move = entered_move)
    
    # Evaluate win
    winning_move = check_winning_board(new_board = new_game_board, winning_board_templates = winning_boards)
    
    # Evaluate end of game
    end_game = not any(map(lambda each: each in new_game_board, [0]))
    
    
    ## Scoring
    if illegal_move == True:
        score = -1
        continue_game = False
        print("Illegal move, automatic loss", "\n", "Score = -1")
    elif winning_move == True:
        score = 1
        continue_game = False
        print("Winning move", "\n", "Score = 1")
    elif (end_game == True and winning_move == False and illegal_move == False):
        score = 0
        continue_game = False
        print("End game, no winners", "\n", "Score = 0")
    else:
        score = 0
        continue_game = True
    
    ## Prep for the next turn
    if continue_game == True:
        # Make the "new" board the game board
        game_board = new_game_board
        # Swap players
        current_player = int(players[players != current_player])


















