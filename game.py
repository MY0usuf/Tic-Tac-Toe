basic_template = '''
 t1| t2| t3
---|---|---
 m1| m2| m3
---|---|---
 b1| b2| b3 
'''
# Declaring  important variables before
X = 'X '
O = 'O '
Winner = False

def print_board(board):
    print(f'''
 {board['t1']}| {board['t2']}| {board['t3']}
---|---|---
 {board['m1']}| {board['m2']}| {board['m3']}
---|---|---
 {board['b1']}| {board['b2']}| {board['b3']} 
''')

def start_game():
    print('Welcome to the tic tac toe game!')
    #print out the basic template of the board
    print(basic_template)
    game_start = input('do want to play the game? y/n >>>')
    if game_start == 'y':
        main_board()
    elif game_start == 'n':
        print('Thank you come again later!')

def check_row(board):
    if board['t1'] == board['t2'] == board['t3'] == X or board['t1'] == board['t2'] == board['t3'] == O:
        return 1
    elif board['m1'] == board['m2'] == board['m3'] == X or board['m1'] == board['m2'] == board['m3'] == O:
        return 1
    elif board['b1'] == board['b2'] == board['b3'] == X or board['b1'] == board['b2'] == board['b3'] == O:
        return 1
    else:
        return 0

def check_col(board):
    if board['t1'] == board['m1'] == board['b1'] == X or board['t1'] == board['m1'] == board['b1'] == O:
        return 1
    elif board['t1'] == board['m2'] == board['b2'] == X or board['t1'] == board['m2'] == board['b2'] == O:
        return 1
    elif board['t3'] == board['m3'] == board['b3'] == X or board['t3'] == board['m3'] == board['b3'] == O:
        return 1
    else:
        return 0

def check_diag_right(board):
    if board['t3'] == board['m2'] == board['b1'] == X or board['t3'] == board['m2'] == board['b1'] == O:
        return 1
    else:
        return 0

def check_diag_left(board):
    if board['t1'] == board['m2'] == board['b3'] == X or board['t1'] == board['m2'] == board['b3'] == O:
        return 1
    else:
        return 0

def check_winner(board):
    if check_diag_right(board) == 1 or check_diag_left(board) == 1 or check_row(board) == 1 or check_col(board):
        return True
    else:
        return False

def winner(current_player):
    if current_player == 'Player1':
        print(f'Winner is {current_player}')
        play_again()
    else:
        print(f'Winner is {current_player}')
        play_again()

def check_draw(total_inputs):
    if total_inputs == 9 and check_winner() == False:
        print('Nobody won!')

def swap_player(current_player):
    if current_player == 'Player1':
        return 'Player2'
    else:
        return 'Player1'

def main_board():
    current_player = 'Player1'
    total_inputs = 0

    # making a dict for board with keys as places in board
    board = {'t1':'  ','t2':'  ','t3':'  ','m1':'  ','m2':'  ','m3':'  ','b1':'  ','b2':'  ','b3':'  '}

    print('Lets start the game\n')
    print('Player1 : O        Player2 : X')
    print_board(board)
    global Winner 
    while total_inputs != 9:
        try:
            player_input = input(f'{current_player}>>>> ')
            if player_input in board:
                if board[player_input] == '  ': # this if block is being used to check whther the input is already present or not
                    if current_player == 'Player1':
                        board[player_input] = O
                        print_board(board)
                        total_inputs += 1
                        Winner = check_winner(board)
                        if Winner == True:
                            winner(current_player)
                            break
                        else:
                            current_player = swap_player(current_player)
                            continue
                    else:
                        board[player_input] = X
                        print_board(board)
                        total_inputs += 1
                        Winner = check_winner(board)
                        if Winner == True:
                            winner(current_player)
                            break
                        else:
                            current_player = swap_player(current_player)
                            continue
        except:
            pass
        check_draw(total_inputs)

def play_again():
    play_again = input('Do you want to play again? y/n: ')
    if play_again.upper() == 'Y':
        start_game()
    else:
        print('Thank you for playing!')
        
start_game()

'''template = 
 {board['t1']}| {board['t2']}| {board['t3']}
---|---|---
 {board['m1']}| {board['m2']}| {board['m3']}
---|---|---
 {board['b1']}| {board['b2']}| {board['b3']} 
'''

'''empty_template = 
   |   |
---|---|---
   |   |
---|---|---
   |   |   
'''
