class Board:
    E = '_'
    X = 'x'
    O = 'o'

    P1 = X
    P2 = O

    def __init__(self):
        self.rows = []
        self.rows.append([self.E, self.E, self.E])
        self.rows.append([self.E, self.E, self.E])
        self.rows.append([self.E, self.E, self.E])

        self.turn = 1
        self.won = False

    def greet(self):
        return print('Welcome! Here is your board')

    def display(self):
        print(self.__str__())

    def __str__(self):
        rows = ', '.join(self.rows[0])+'\n'
        rows += ', '.join(self.rows[0])+'\n'
        rows += ', '.join(self.rows[0])
        return rows


def test_new_board():
    b = Board()
    assert b.__str__() == '''_, _, _
_, _, _
_, _, _'''


def test_uppercase():
    assert "test".upper() == 'TEST'


if __name__ == '__main__':
    b = Board()
    # print(b)
    b.greet()
    b.display()
