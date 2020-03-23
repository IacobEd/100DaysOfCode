import random


class TicTacToe:
    def __init__(self):
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def show(self):
        print("""
         -------------
         | {} | {} | {} |
         -------------
         | {} | {} | {} |
         -------------
         | {} | {} | {} |
         -------------
        """.format(*self.board))

    def clearBoard(self):
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def whoWon(self):
        if self.checkWin() == "X":
            return "X"
        elif self.checkWin() == "O":
            return "O"
        elif self.gameOver() == True:
            return "Nobody"

    def availableMoves(self):
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def getMoves(self, player):
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    def makeMove(self, position, player):
        # if(player == 'X'):
        #     if(self.board[position] == 'X'):
        #         playerMove = int(input('That block is already occupied, choose another one: '))
        #         self.makeMove(self, board[playerMove] - 1, player)
        # else:
        self.board[position] = player

    def checkWin(self):
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getMoves(player)
            for combo in combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def gameOver(self):
        if self.checkWin() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    def minimax(self, board, depth, player):
        if depth == 0 or board.gameOver():
            if board.checkWin() == "X":
                return 0
            elif board.checkWin() == "O":
                return 100
            else:
                return 50

        if player == "O":
            bestValue = 0
            for move in board.availableMoves():
                board.makeMove(move, player)
                moveValue = self.minimax(board, depth - 1, changePlayer(player))
                board.makeMove(move, " ")
                bestValue = max(bestValue, moveValue)
            return bestValue

        if player == "X":
            bestValue = 100
            for move in board.availableMoves():
                board.makeMove(move, player)
                moveValue = self.minimax(board, depth - 1, changePlayer(player))
                board.makeMove(move, " ")
                bestValue = min(bestValue, moveValue)
            return bestValue


def changePlayer(player):
    if player == "X":
        return "O"
    else:
        return "X"


def make_best_move(board, depth, player):
    best = 50
    choices = []
    for move in board.availableMoves():
        board.makeMove(move, player)
        moveValue = board.minimax(board, depth - 1, changePlayer(player))
        board.makeMove(move, " ")

        if moveValue > best:
            choices = [move]
            break
        elif moveValue == best:
            choices.append(move)
    print("choices: ", choices)

    if len(choices) > 0:
        return random.choice(choices)
    else:
        return random.choice(board.availableMoves())


if __name__ == '__main__':
    game = TicTacToe()
    game.show()
    y = 1

    while y == 1:
        while game.gameOver() == False:
        #while
            try:
                person_move = int(input("You are X: Choose number from 1-9: "))
            except:
                print('You want to play games with me huh? Is that simple '
                      'a number from 1-9, that''s it')
                person_move = int(input("Let's try it again (from 1-9): "))

            game.makeMove(person_move - 1, "X")
            game.show()

            if game.gameOver() == True:
                break

            print("Computer choosing move...")
            ai_move = make_best_move(game, -1, "O")
            game.makeMove(ai_move, "O")
            game.show()

        aiBot = game.whoWon()
        if (aiBot == 'O'):
            print('A robot just beat yoo ass .. pff , pathetic')
        elif (aiBot == 'X'):
            print("You won *slow clapping*")
        elif (aiBot == 'Nobody'):
            print('You got lucky this time, the almighty AI had mercy , nodoby wins')

        try:
            y = int(input("Dou you want to play again, Yes(1) No(0): "))
        except:
            print('You picked anything else except 1 or 0 , right?')
            y = int(input("Just pick 1 or 0 .. please!: "))

        if (y == 0):
            print('Bye bye, fella')
            break
        game.clearBoard()
        game.show()
