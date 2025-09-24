# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    quincy_pattern = ['R', 'R', 'P', 'P', 'S']
    ideal_plays = {'P': 'S', 'R': 'P', 'S': 'R'} 

    guess = "R"
    if len(opponent_history) > 4 and (opponent_history[:5] == quincy_pattern):
        print ("Detected Quincy!")
        last_two = opponent_history[-2:]
        if last_two == ['P', 'P']:
            guess = ideal_plays['S']
        elif last_two == ['R', 'R']:
            guess = ideal_plays['P']
        elif last_two == ['P', 'S']:
            guess = ideal_plays['R']
        else:
            guess = ideal_plays[opponent_history[-1]]

       

    return guess
