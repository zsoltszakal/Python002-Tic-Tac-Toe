board = {"1": " ", "2": " ", "3": " ",
         "4": " ", "5": " ", "6": " ",
         "7": " ", "8": " ", "9": " "}

def game_board():
    print("-----------")
    print(board["1"] + " | " + board["2"] + " | " + board["3"])
    print("-----------")
    print(board["4"] + " | " + board["5"] + " | " + board["6"])
    print("-----------")
    print(board["7"] + " | " + board["8"] + " | " + board["9"])
    print("-----------")


def game():
    game_board()


    turn = "X"
    count = 0

    for i in range(10):
        move = input(f"It is your turn '{turn}' - Which place to move?\n")
        if board[move] == " ":
             board[move] = turn
             count += 1
        else:
            print(f"That place is already in use '{turn}'")
            continue

        game_board()

        if count >= 5:
            if board["1"] == board["2"] == board["3"] != " ":
                print("\nGame over\n")
                print(f"You win '{turn}'")
                break
            elif board["1"] == board["4"] == board["7"] != " ":
                print("\nGame over\n")
                print(f"You win '{turn}'")
                break
            elif board["4"] == board["5"] == board["6"] != " ":
                print("\nGame over\n")
                print(f"You win '{turn}'")
                break
            elif board["7"] == board["8"] == board["9"] != " ":
                print("\nGame over\n")
                print(f"You win '{turn}'")
                break
            elif board["2"] == board["5"] == board["8"] != " ":
                print("\nGame over\n")
                print(f"You win '{turn}'")
                break
            elif board["3"] == board["6"] == board["9"] != " ":
                print("\nGame over\n")
                print(f"You win '{turn}'")
                break
            elif board["1"] == board["5"] == board["9"] != " ":
                print("\nGame over\n")
                print(f"You win '{turn}'")
                break

        if count == 9:
            print("\nGame over\n")
            print("It is a tie")

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    restart_game = input("Would you like to play again? (y/n)")
    if restart_game == "y" or restart_game == "Y":
        for key in board:
            board[key] = " "

        game()

game()
