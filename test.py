import itertools

def print_map(game_map):
	print("   0  1  2  3")
	for count, rows in enumerate(game_map):
		print(count, rows)

def select_size_of_game():
	n = int(input(f'Please select the size: '))
	gameselect = [[0 for i in range(n)] for j in range(n)]
	print_map(gameselect)
	return gameselect

def wingame(game):
	#horizontally
	for row in game:
		if row.count(row[0]) == len(row) and row[0] != 0:
			print("The person",row[0],"Winn!")
			return True
	#vertically
	for col in range(len(game)):
		check = []
		for row in game: 
			check.append(row[col]) #rotate
		if check.count(check[0]) == len(game) and check[0] != 0:
			print("The person",check[0],"Winn!")
			return True
	#diagonally\
	diag = []
	for dix in range(len(game)):
		diag.append(game[dix][dix])
	if diag.count(diag[0]) == len(game) and diag[0] != 0:
		print("The person",diag[0],"Winn!")
		return True
	#diagonally/
	diag = []
	for rows, cols in enumerate(reversed(range(len(game)))):
		diag.append(game[rows][cols])
	if diag.count(diag[0]) == len(game) and diag[0] != 0:
		print("The person",diag[0],"Winn!")
		return True

def game_board(game_map, players = 0, row = 0, column = 0, display_game = False):
	try:
		if game_map[row][column] != 0:
			print(f'Error!! Index has been selected, try select another index')
			print(f"current_player {players}")
			print_map(game_map)
			return game_map, False
		game_map[row][column] = players
		print_map(game_map)
		return game_map, True
	except IndexError: #you dont need as e here, unless you are going to use any IndexError functions
		print(f'Error!! outrange index, try again')
		return game_map, False
	
def play_game(game):
	player_choice = itertools.cycle([1, 2])
	game_won = False
	while not game_won:
		current_player = next(player_choice)
		print(f"current_player {current_player}")
		played = False
		while not played:
			row_choice = int(input(f'Select the row index: '))
			column_choice = int(input(f'Select the culumn index: '))
			game, played = game_board(game, current_player, row_choice, column_choice)
		game_won = wingame(game)
	# return None # dont need to return anything if you have nothing to return. 

if __name__ == "__main__":
    game_stop = False
    while not game_stop:
	    play_game(select_size_of_game())
	    ans = input('Do you want play again? (Y/N) ')
	    if ans.upper() == 'N':
		    game_stop = True
		    print("Bye bye!")