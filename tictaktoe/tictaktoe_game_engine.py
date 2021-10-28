class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = [',' + self.SIZE * self.SIZE]
        self.turn = 'x'

    def show_board(self):
        print(self.board)

    def set(self,row,col): # 1,1=0 1,2=1 1,3=2
        pass

    def set_winner(self):
        pass
        # - 3줄
        # | 3줄
        # / 3줄
        # \ 3줄
        return self.turn
        # 비기는 조건. 다 채워졌을때 위의 조건이 해당X: self.board에 '.'이 없어야함
        return '0'

    def change_turn(self):
        # self.turn 'X'일땐 '0'  '0'일땐 'X'
        pass


if __name__ == '__main__':
    game_engine = TictactoeGameEngine
    game_engine.show_board()
    game_engine.set(3,2)
    game_engine.show_board()
    game_engine.set(3,1)
    game_engine.set(3,3)
    print(game_engine.set_winner())
    game_engine.change_turn()
    print(game_engine.turn)

