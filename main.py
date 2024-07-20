import copy

def user_input(player) -> str:
    '''
    Function to gather user input.
    '''
    if player % 2:
        return input('Player two, insert location for your X:\n>>> ').upper()
    else:
        return input('Player one, insert location for your O:\n>>> ').upper()

def input_correction(location, player_count, table) -> str:
    '''
    Function to verify user input.
    '''
    valid_locations = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    while location not in valid_locations or table[location[0]][int(location[1]) - 1] != '| ':
        print('Wrong location. Try again\n>>> ')
        location = user_input(player_count)
    
    return location

def table():
    '''
    Function to create the game board.
    '''
    return {' ': ['|1', '|2', '|3', '| '], 'A': ['| ', '| ', '| ', '| '], 'B': ['| ', '| ', '| ', '| '], 'C': ['| ', '| ', '| ', '| ']}

def split_string(s):
    '''
    Function to split user input into row and column.
    '''
    return [s[0], s[1:]]

def table_update(table, user_input, player):
    '''
    Function to update the game board with the player's move.
    '''
    row, col = user_input
    column_index = int(col) - 1  
    if player % 2:
        table[row][column_index] = '|X'
    else:
        table[row][column_index] = '|O'
    return table

def new_table(table):
    '''
    Function to print the game board.
    '''
    table_rows = []
    for key, value in table.items():
        rows = key + ''.join(value)
        table_rows.append(rows)
    return '\n'.join(table_rows)

def table_preparation_win(table_dict):
    '''
    Function to prepare the table for checking the winning condition.
    '''
    rows = list(table_dict.values())[1:]  
    rows = copy.deepcopy(rows)
    lines = []
    lines.extend(rows)
    columns = [[row[i] for row in rows] for i in range(len(rows[0]))]
    lines.extend(columns)
    diagonal = [rows[i][i] for i in range(len(rows))]
    diagonal_rev = [rows[i][len(rows) - 1 - i] for i in range(len(rows))]
    lines.extend([diagonal, diagonal_rev])
    return lines

def winning_condition(conditions):
    '''
    Function to check if a player has won.
    '''
    for line in conditions:
        if all(pos == '|X' for pos in line):
            print('Player X is the winner!!!')
            return True
        if all(pos == '|O' for pos in line):
            print('Player O is the winner!!!')
            return True
    return False

def pat(conditions):
    '''
    Function to check if the game is a draw.
    '''
    line = ''.join([''.join(x) for x in conditions])
    for x in line:
        if x == '| ':
            break
    else:
        return True
    return False

def run():
    player_count=0
    game_table = table()
    
    while True:
        input_str = input_correction(user_input(player_count), player_count, game_table)
        split_input = split_string(input_str)
        game_table = table_update(game_table, split_input, player_count)
        print(new_table(game_table))
        preparation_str = table_preparation_win(game_table)
        
        if winning_condition(preparation_str):
            break
        elif pat(preparation_str) and player_count >= 8: 
            print("The game is a draw!")
            break
        player_count += 1
        
if __name__ == '__main__':
    run()