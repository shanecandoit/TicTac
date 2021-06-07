from typing import List


class Board:
    E: str = '_'
    X: str = 'x'
    O: str = 'o'

    P1: str = 'Player1 (X)'
    P2: str = 'Player2 (O)'

    def __init__(self):
        self.rows: List[List[str]] = []
        self.rows.append([self.E, self.E, self.E])
        self.rows.append([self.E, self.E, self.E])
        self.rows.append([self.E, self.E, self.E])

        self.turn: int = 1
        self.won: bool = False
        self.player: str = self.P1

    def greet(self) -> None:
        print('Welcome! Here is your board')

    def prompt_turn(self, input_str=None) -> (int, int):
        print(self.player, 'where would you like to move ')
        if not input_str:
            line = input('> ')
        else:
            line = input_str
        print('#', line)
        assert ' ' in line, 'input must be two numbers 1-3 separated by space'
        x, y = 0, 0
        try:
            n1, n2 = line.split()[0], line.split()[1]
            x, y = int(n1), int(n2)
            print(f'x {x} y {y}')
        except Exception as e:
            print(e)
        assert x >= 1 and x <= 3, 'first digit must be 1,2, or 3'
        assert y >= 1 and y <= 3, 'second digit must be 1,2, or 3'
        return x, y

    def next(self, input_str=None):

        # input
        x, y = self.prompt_turn()

        # legal move?
        # if valid_move(x,y)
        #    # update board
        #    move(x,y)
        self.move(x,y,self.player)

        # advance state
        self.turn += 1
        if self.player == self.P1:
            self.player = self.P2
        elif self.player == self.P2:
            self.player = self.P1
        else:
            assert False, "self.player must be self.P1 or self.P2"

    def move(self, x:int, y:int, player=X):
        assert x in [1, 2, 3]
        assert y in [1, 2, 3]
        assert player in [Board.X, Board.E, Board.O]
        self.rows[y-1][x-1] = player
        return str(self)

    def display(self):
        print(self.__str__())
        print()

    def __str__(self):
        rows = ', '.join(self.rows[0]) + '\n'
        rows += ', '.join(self.rows[1]) + '\n'
        rows += ', '.join(self.rows[2])
        return rows

    def is_won(self) -> (bool,str):
        """ is a board won? if so who won? """
        r0 = self.rows[0]
        r1 = self.rows[1]
        r2 = self.rows[2]

        # horizontal
        if r0[0] != Board.E and r0[0] == r0[1] == r0[2]:
            return True, r0[0]
        elif r1[0] != Board.E and r1[0] == r1[1] == r1[2]:
            return True, r1[0]
        elif r2[0] != Board.E and r2[0] == r2[1] == r2[2]:
            return True, r2[0]

        # vertical
        elif r0[0] != Board.E and r0[0] == r1[0] == r2[0]:
            return True, r0[0]
        elif r0[1] != Board.E and r0[1] == r1[1] == r2[1]:
            return True, r0[1]
        elif r0[2] != Board.E and r0[2] == r1[2] == r2[2]:
            return True, r0[2]

        # diagonal
        elif r0[0] != Board.E and r0[0] == r1[1] == r2[2]:  # \
            return True, r0[0]
        elif r0[2] != Board.E and r0[2] == r1[1] == r2[0]:  # /
            return True, r0[2]

        return False, None


if __name__ == '__main__':
    b = Board()
    # print(b)
    b.greet()
    b.display()

    #b.next()
    b.move(1,1,Board.X)
    b.display()

    #b.next()
    b.move(2, 2, Board.O)
    b.display()
