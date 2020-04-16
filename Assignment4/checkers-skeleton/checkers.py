'''
@author: mroch
'''

# Game representation and mechanics
from timer import Timer
import boardlibrary  # might be useful for debugging
import human
from checkerboard import *

# tonto - Professor Roch's not too smart strategy
# You are not given source code to this, but compiled .pyc files
# are available for Python 3.7 and 3.8 (fails otherwise).
# This will let you test some of your game logic without having to worry
# about whether or not your AI is working and let you pit your player
# against another computer player.
#
# Decompilation is cheating, don't do it.  Big sister is watching you :-)

# Python cand load compiled modules using the imp module (deprecated)
# We'll format the path to the tonto module based on the
# release of Python.  Note that we provided tonto compilations for Python 3.7
# and 3.8.  If you're not using one of these, it won't work.
import imp
import sys
major = sys.version_info[0]
minor = sys.version_info[1]
modpath = "__pycache__/tonto.cpython-{}{}.pyc".format(major, minor)
tonto = imp.load_compiled("tonto", modpath)


# human - human player, prompts for input

def timeelapsed(self):
    t = Timer()
    elapsed = t.elapsed_s()


def Game(red=human.Strategy, black=tonto.Strategy,
         maxplies=10, init=None, verbose=True, firstmove=0):
    """Game(red, black, maxplies, init, verbose, turn)
    Start a game of checkers
    red,black - Strategy classes (not instances)
    maxplies - # of turns to explore (default 10)
    init - Start with given board (default None uses a brand new game)
    verbose - Show messages (default True)
    firstmove - Player N starts 0 (red) or 1 (black).  Default 0. 
    """

    # Don't forget to create instances of your strategy,
    # e.g. black('b', checkerboard.CheckerBoard, maxplies)

    red_strategy = red('r', CheckerBoard, maxplies)
    black_strategy = black('b', CheckerBoard, maxplies)

    turn = firstmove
    board = CheckerBoard()
    winner = None
    while not board.is_terminal()[0]:
        if turn is 0:
            if verbose:
                print("Red Player's Turn")
                print("Utility: {}".format(red_strategy.utility(board)))
            board, action = red_strategy.play(board)
            if action is None:
                if verbose:
                    print("Red Player has given up!")
                winner = 'b'
                break
        else:
            if verbose:
                print("Black Player's Turn")
                print("Utility: {}".format(black_strategy.utility(board)))
            board, action = black_strategy.play(board)
            if action is None:
                if verbose:
                    print("Black Player has given up!")
                winner = 'r'
                break

        turn = (turn + 1) % 2
        if turn % 2 == 0:
            if verbose:
                print("End of Cycle")
                print(board)
                print("\n\n")

    if board.is_terminal()[0]:
        winner = board.is_terminal()[1]
        if winner is None:
            print("Game over! Result: Draw")
        else:
            print("Game over! - {} wins".format(winner))
    else:
        print("Player Forfeited - {} wins!".format(winner))


if __name__ == "__main__":
    # Game(init=boardlibrary.boards["multihop"])
    # Game(init=boardlibrary.boards["StrategyTest1"])
    #Game(init=boardlibrary.boards["EndGame1"], firstmove = 1)
    Game()
