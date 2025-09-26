# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    quincy_pattern = ['R', 'R', 'P', 'P', 'S']
    kris_pattern = ['P', 'P', 'S', 'R', 'P']
    mrugesh_pattern = ['R', 'R', 'R', 'R', 'P']
    ideal_plays = {'P': 'S', 'R': 'P', 'S': 'R'} 
    moves = ['R', 'P', 'S']

    print(opponent_history[0:20])
    guess = moves[(len(opponent_history) - 1) % 3]
    if len(opponent_history) > 10 and (opponent_history[5:10] == quincy_pattern):
        last_two = opponent_history[-2:]
        if last_two == ['P', 'P']:
            guess = ideal_plays['S']
        elif last_two == ['R', 'R']:
            guess = ideal_plays['P']
        elif last_two == ['P', 'S']:
            guess = ideal_plays['R']
        else:
            last_move = opponent_history[-1]
            if last_move == '':
                guess = 'P'  # Default move for first turn
            else:
                guess = ideal_plays[last_move]
    elif len(opponent_history) > 1 and (opponent_history[1:6] == kris_pattern):
        moves2 = ['S', 'P', 'R']
        guess = moves2[(len(opponent_history) - 1) % 3]
    elif len(opponent_history) > 1 and (opponent_history[1:6] == mrugesh_pattern):
        guess = ideal_plays[opponent_history[-1]]
    

    return guess
