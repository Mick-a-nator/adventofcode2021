from typing import List
from collections import namedtuple


Square = namedtuple('Square', ['num', 'called'])

class BingoBoard():
    def __init__(self, nums: List[List[str]]):
        self.board = [[Square(num=int(num), called=False) for num in row] for row in nums]
    
    def __repr__(self):
        return '<<' + '\n'.join([','.join(['x' if sq.called else str(sq.num) for sq in row]) for row in self.board]) + '>>\n'

    def call(self, num: int):
        for x in range(5):
            for y in range(5):
                if self.board[x][y].num == num:
                    self.board[x][y] = Square(num = self.board[x][y].num, called = True)
                    return
    
    def bingo_row(self) -> bool:
        for row in self.board:
            if all([square.called for square in row]):
                return True
        return False
    
    def bingo_col(self):
        for colNum in range(5):
            col = [row[colNum] for row in self.board]
            if all([square.called for square in col]):
                return True
        return False
    
    def bingo_diag1(self):
        return all([self.board[i][i].called for i in range(5)])
    
    def bingo_diag2(self):
        return all([self.board[4 - i][i].called for i in range(5)])
    
    def bingo(self):
        return any([
            self.bingo_row(),
            self.bingo_col(),
        ])

    def uncalled_sum(self):
        sum = 0
        for row in self.board:
            for sq in row:
                if not sq.called:
                    sum += sq.num
        return sum
    

def play(boards: List[BingoBoard], calls: List[int]):
    for call in calls:
        for board in boards:
            board.call(call)
            if board.bingo():
                sum = board.uncalled_sum()
                print(f"{sum} * {call} = {sum * call}")
                return
    print('No bingo!')
    
def last_by_comprehensions(boards: List[BingoBoard], calls: List[int]):
    for num in calls:
        for board in boards:
            board.call(num)
        boards = [board for board in boards if not board.bingo()]
        if len(boards) == 1:
            return boards[0].uncalled_sum() * num
        
def every_bingo(boards: List[BingoBoard], calls: List[int]):
    for num in calls:
        for i, board in enumerate(boards):
            if board is not None:
                board.call(num)
                if board.bingo():
                    print(board.uncalled_sum() * num)
                    boards[i] = None

# def last_bingo(boards: List[BingoBoard], calls: List[int]):
#     for call in calls:
#         for board in boards:
#             board.call(call)
#             if board.bingo():
#                 if len(boards) > 1:
#                     boards.remove(board)
#                 elif len(boards) == 1:
#                     print(board)
#                     return boards[0].uncalled_sum() * call
    
# def play_last_board(last:BingoBoard, calls):
#     print(last)
#     for call in calls:
#         last.call(call)
#         if last.bingo():
#             sum = last.uncalled_sum()
#             print(f"{sum} * {call} = {sum * call}")
#             return

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
 
with open('Day4/input.txt') as input:
    calls = [int(n) for n in input.readline().split(',')]
    
    all_boards = [BingoBoard([row.split() for row in chunk[1::]]) for chunk in chunker(input.readlines(), 6)]
    
    # play(all_boards, calls)
    last_board = last_by_comprehensions(all_boards, calls)
    # play_last_board(last_board, calls)
    print(last_board)
    every_bingo(all_boards, calls)

