import copy
import random


class AI():
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0 , len(empty_sqrs))

        return empty_sqrs[idx]
    
    def minimax(self, board, maximizing):
        case = board.final_state()

        if case == 1:
            return 1, None
        if case == 2:
            return -1, None
        elif board.is_full():
            return 0, None
        
        if maximizing:
            max_eval = -2
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        elif not maximizing:
            min_eval = 2
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move
        

    def eval(self, main_board):
        if self.level == 0:
            eval = 'random'
            move = self.rnd(main_board)
        else:
            eval, move = self.minimax(main_board, False)
        
        print(f"AI has chosen to mark the square in pos {move} with an eval of {eval}")

        return move