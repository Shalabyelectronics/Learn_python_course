from os import system


# First we need to create a draw_board Function that draw the tic tac toa board
def draw_board() -> str:
    """
    This Function will draw a tic tac toa board by changing # to the player chosen sympol O or X
    """
    col_rows = {
            "r1":[" "," ", " ", "|"," ", " ", " ","|"," ", " ", " "],
            "e1":[" ","1", " ", "|"," ", "2", " ","|"," ", "3", " "], 
            "r2":["_","_", "_", "|","_", "_", "_","|","_", "_", "_"],
            "e2":[" ","4", " ", "|"," ", "5", " ","|"," ", "6", " "], 
            "e3":[" ","7", " ", "|"," ", "8", " ","|"," ", "9", " "], 
            }
    return col_rows


# Second I need to get player one and player two sympol selection for each one and thier names as well
def get_players_info(position:str="player",other_player:dict={}) -> dict:
    """This Function will create a player info dictionary that include player name and what his sympol"""
    player_name = input(f"\n>>> Hi player {position} , What is your name? ").title()
    player_sympol = None
    if other_player == {}:
        while True:
            player_sympol = input(f"\n>>> Ok {player_name}, What do you want to choose (X) or (O) : ").upper()
            # only X or O
            if player_sympol not in ["X", "O"]:
                print(f"{player_name}, please choose (X) or (O) only!!! ")
            else:
                break
    elif other_player["sympol"] == "X":
        player_sympol = "O"
        print(f"\n>>> {player_name} you will got {player_sympol}, because {other_player['name']} got {other_player['sympol']}.")
    else:
        player_sympol = "X"
        print(f"\n>>> {player_name} you will got {player_sympol}, because {other_player['name']} got {other_player['sympol']}.")
    return {"name" : player_name, "sympol" : player_sympol, "move":[], "wins":0}

def edit_activeboard_dict(active_board:dict, player:dict)->dict:
    for move in player["move"]:
        for value in active_board.values():
            if move in value:
                value[value.index(move)] = player["sympol"]


def update_active_board(active_board:dict,player1:dict, player2:dict)-> dict:
    # Add player one sympol on the board
    edit_activeboard_dict(active_board,player1)
    edit_activeboard_dict(active_board,player2) 
    print(
            "".join(active_board["r1"]),
            "".join(active_board["e1"]),
            "".join(active_board["r2"]),
            "".join(active_board["r1"]),
            "".join(active_board["e2"]),
            "".join(active_board["r2"]),
            "".join(active_board["e3"]),
            "".join(active_board["r1"]),
            sep="\n") 

def get_player_choice(player:dict,choosed_list:list)->dict:
    player_choice = input(f"Your turn {player['name']} type position number -> ")
    # check if the choice is available
    while True:
        if player_choice not in choosed_list and player_choice in [str(n) for n in range(1,10)]:
            player["move"].append(player_choice)
            choosed_list.append(player_choice)
            break
        else:
            print(f"The position number {player_choice} is not a vailable.")
            player_choice = input("Please chose another position number.")
    return player

def is_winner(player:dict)->bool:
    winner_casses = {
            "c1":['1','2','3'],
            "c2":['1','5','9'],
            "c3":['1','4','7'],
            "c4":['2','5','8'],
            "c5":['3','5','7'],
            "c6":['3','6','9'],
            "c7":['4','5','6'],
            "c8":['7','5','3'], 
            "c9":['7','8','9'],
            }
    result = None
    for plan in winner_casses.values():
        points = []
        for move in player['move']:
            if move in plan:
                points.append(True)
            else:
                points.append(False)
        if points.count(True) == 3:
            result = True
            break
        else:
            result = False
    return result

def is_tie(chosed_positions:list, is_winner:bool)->bool:
    if len(chosed_positions) == 9 and is_winner == False:
        return True
    return False

def draw_score_board(player1:dict, player2:dict)->dict:
    print("*"* (len(player1['name']) + len(player2['name']) + 13))
    print(">"*3, f"{player1['name']}","|"*2, f"{player2['name']}", "<"*3)
    print("["*3,f"{str(player1['wins']).center(len(player1['name']))}","-"*2, f"{str(player2['wins']).center(len(player2['name']))}", "]"*3)
    print("*"* (len(player1['name']) + len(player2['name']) + 13))

def reset_game_board_move(player1:dict,player2:dict,chosed_positions:list, active_board):
    player1['move'].clear()
    player2['move'].clear()
    chosed_positions.clear()
    active_board = draw_board()


def game(play_again:bool=False, chosed_positions:list=[],player_one_dict:dict={},player_two_dict:dict={},active_board:dict={}):
    #if the player want to revange so I need to skip getting the player data
    print("\n\nWelcome to Shalaby tic tac toa Game","_"*36,sep="\n")
    if play_again == False:    
        chosed_positions = []
        player_one_dict = get_players_info("one")
        player_two_dict = get_players_info("two", player_one_dict)
        active_board = draw_board()
        
    while True:
        system("clear")
        draw_score_board(player_one_dict, player_two_dict)
        update_active_board(active_board,player_one_dict,player_two_dict)
        if is_winner(player_two_dict):
            print(f"Woow, {player_two_dict['name']} you are the Winner!!!")
            do_revange = input(f"Oops {player_two_dict['name']} do you want to revange from your lost? (Y) (N) ").lower()
            if do_revange == "y":
                system("clear")
                player_two_dict['wins'] += 1
                player_one_dict['move'] = []
                player_two_dict['move'] = []
                chosed_positions = []
                active_board = draw_board()
                game(True,chosed_positions,player_one_dict,player_two_dict,active_board)
            else:
                break
        if is_tie(chosed_positions,is_winner(player_two_dict)):
            do_challenge = input(f"It is tie, {player_two_dict['name']} Do you yant to challenge {player_one_dict['name']} Again (Y) or (N)").lower()
            if do_challenge == 'y':
                system("clear")
                player_one_dict['move'] = []
                player_two_dict['move'] = []
                chosed_positions = []
                active_board = draw_board()
                game(True,chosed_positions,player_one_dict,player_two_dict,active_board)
                """
                reset_game_board_move(player_one_dict,
                        player_two_dict,
                        chosed_positions,
                        active_board)
                """
            else:
                break
            
        get_player_choice(player_one_dict, chosed_positions)
        system("clear")
        draw_score_board(player_one_dict, player_two_dict)
        update_active_board(active_board,player_one_dict,player_two_dict)
        if is_winner(player_one_dict):
            print(f"Woow, {player_one_dict['name']} you are the Winner!!!")
            do_revange = input(f"Oops {player_two_dict['name']} do you want to revange from your lost? (Y) (N) ").lower()
            if do_revange == "y":
                system("clear") 

                player_one_dict['wins'] += 1
                player_one_dict['move'] = []
                player_two_dict['move'] = []
                chosed_positions = []
                active_board = draw_board()
                game(True,chosed_positions,player_one_dict,player_two_dict,active_board)
            else:
                break
        if is_tie(chosed_positions,is_winner(player_two_dict)):
            do_challenge = input(f"It is tie, {player_one_dict['name']} Do you yant to challenge {player_two_dict['name']} Again (Y) or (N)").lower()
            if do_challenge == 'y':
                system("clear")
                player_one_dict['move'] = []
                player_two_dict['move'] = []
                chosed_positions = []
                active_board = draw_board()

                game(True,chosed_positions,player_one_dict,player_two_dict,active_board)
            else:
                break
        get_player_choice(player_two_dict, chosed_positions)


game()       
