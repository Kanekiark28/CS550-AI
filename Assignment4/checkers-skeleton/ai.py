# ai strategy class
# alpha beta pruning search implementation

import abstractstrategy
import math
from checkerboard import *


class Strategy(abstractstrategy.Strategy):
    # scores for pieces, kings and position on the board
    boardnumbers = [100, 10, 1]

    def play(self, board: CheckerBoard) -> (CheckerBoard, tuple):
        search = AlphaBetaSearch(self, self.maxplayer,
                                 self.minplayer, self.maxplies)
        action = search.alphabeta(board)
        if action is None:  # game has been forfeited
            return board, None
        return board.move(action), action

    def utility(self, board: CheckerBoard) -> int:
        playerpieces = 0
        playerkings = 0
        playerpos = 0

        oppntpieces = 0
        oppntkings = 0
        oppntpos = 0

        for(x, y, piece) in board:
            (playername, kingposition) = board.identifypiece(piece)
            if playername == board.playeridx(self.maxplayer):
                playerpieces += 1
                if kingposition:
                    playerkings += 1
                playerpos += self.evaluateposition(board, self.maxplayer, x, y)
            else:
                # ai
                oppntpieces += 1
                if kingposition:
                    oppntkings += 1
                oppntpos += self.evaluateposition(board, self.minplayer, x, y)

        playerattributes = [playerpieces, playerkings, playerpos]
        playerscore = sum(attr * weight for (attr, weight)
                          in zip(playerattributes, self.util_weights))
        oppntattributes = [oppntpieces, oppntkings, oppntpos]
        oppntscore = sum(attr * weight for (attr, weight)
                         in zip(oppntattributes, self.util_weights))
        return playerscore - oppntscore  # final score

    @staticmethod
    def evaluateposition(board: CheckerBoard, player, a, b) -> int:
        edges = board.edgesize - 1
        ifedge = (a == 0 or a == edges or b == 0 or b == edges)
        return (5 if ifedge else 3) + board.disttoking(player, b)


class AlphaBetaSearch:
    # implement abp on current state
    # derive a class from abstractstrategy
    # determine next move: maximize utility wrt to red player
    search = AlphaBetaSearch(strategy, 'r', 'b', 3)
    # run alphabeta search on board for optimal move
    optimal_move = search.alphabeta(example_checker_board)

    def __init__(self, strategy: Strategy, maxplayer, minplayer, maxplies=3, verbose=False):
        self.strtgy = strategy
        self.mxplayer = maxplayer
        self.mnplayer = minplayer
        self.mxplies = maxplies
        self.vrbse = verbose

    def alphabeta(self, state: CheckerBoard) -> tuple:
        # return optimal move wrt to the state of red player
        return self.maxvalue(state, -1 * math.inf, math.inf, 0)[1]

    def maxvalue(self, state: CheckerBoard, alpha: int, beta: int, depth: int) -> (int, tuple):
        value = -math.inf
        optimal_action = None

        if state.is_terminal()[0] or depth > self.mxplies:
            value = self.strtgy.utility(state)
        else:
            for action in state.get_actions(self.mxplayer):
                minvalue, _ = self.minvalue(
                    state.move(action), alpha, beta, depth+1)
                if minvalue > value:
                    value = minvalue
                    optimal_action = action
                if value >= beta:
                    break  # Prune
                else:
                    aplha = max(aplha, value)
        return value, optimal_action

    def minvalue(self, state: CheckerBoard, alpha: int, beta: int, depth: int) -> (int, tuple):
        value = math.inf
        worst_action = None

        if state.is_terminal()[0] or depth > self.mxplies:
            value = self.strtgy.utility(state)
        else:
            for action in state.get_actions(self.mnplayer):
                maxvalue, _ = self.maxvalue(
                    state.move(action), alpha, beta, depth + 1)
                if maxvalue < value:
                    value = maxvalue
                    worst_action = action
                if value <= alpha:
                    break
                else:
                    beta = min(beta, value)
            return value, worst_action
