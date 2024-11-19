# Tic Tac Toe game

# State storage.
#       list to store the game state, with each member of the list are the value of each box of the game

# Game play
#       a function which outputs the game interface
#       A function update the game state
#       A function that check for a winner

playing = True

player_turn = 1

game_state = [[ 0 , 1 , 2 ],
              [ 3 , 4 , 5 ],
              [ 6 , 7 , 8 ] ]

game_control = {
    '0': [0, 0],
    '1': [0, 1],
    '2': [0, 2],
    '3': [1, 0],
    '4': [1, 1],
    '5': [1, 2],
    '6': [2, 0],
    '7': [2, 1],
    '8': [2, 2],
}

player1 = 'X'
player2 = 'O'

# a function which outputs the game interface
def command_interface():
    for row in game_state:
        print('_'*20)
        line = ""
        for value in row:
            line += f"  {value}  |"
        print(line)
    print('_'*20)

#       A function that check for a winner
def check_win_draw():
    # Possible win combination
    hor_0 = [row[0] for row in game_state]
    hor_1 = [row[1] for row in game_state]
    hor_2 = [row[2] for row in game_state]
    cross_section = [[game_state[0][0], game_state[1][1], game_state[2][2]],
                     [game_state[0][2], game_state[1][1], game_state[2][0]]]
    horizontal = [list(hor_0), list(hor_1), list(hor_2)]

    draw_index = 0
    winning_combination = [game_state, cross_section, horizontal]

    for combination in winning_combination:
        for row in combination:
            if row[0] == row[1] == row[2]:
                return "Won"
            else:
                if winning_combination.index(combination) == 0:
                    for value in row:
                        if value in ('X','O'):
                            draw_index += 1
            if draw_index == 9:
                return 'Draw'
    return "Play"




#       A function to update the game state
def update_game_state(player, position):

    if game_state[position[0]][position[1]] not in ('X','O'):
        game_state[position[0]][position[1]] = player
        return True
    else:
        return False


# The function to run the process of the game.
def engine():
    print(f'player-{player} turn')
    position = input("Please enter the index of the box you want to fill> ")
    if position not in ('0','1','2','3','4','5', '6','7','8'):
        print("Please enter a valid index number!!! ")
    else:
        global player_turn
        global playing

        success = update_game_state(player, game_control[position])
        if success:
            player_turn += 1
            command_interface()
            print('\n')
            win_draw = check_win_draw()
            if win_draw == 'Won':
                print(f'Congratulations to Player-{player}, You Won!!!')
                playing = False
                input('Press Enter To Continue!! ')

            elif win_draw == 'Draw':
                print("Match is a Draw!!!!!")
                playing = False
                input('Press Enter To Continue!! ')

            else:
                input('Press Enter To Continue!! ')




if __name__ == '__main__':
    print("Tic Tac Toe!!")
    command_interface()
    print('\n')
    while playing:
        if player_turn % 2 == 1:
            player = player1
        else:
            player = player2
        engine()