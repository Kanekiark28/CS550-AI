'''
driver for graph search problem
'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies

# Create 31 Trials
# For each Trial, Use BFS, DFS, A* using Manhattan Distance
# Keep track of the nodes expanded through -> Frontier set? and amount of time
# Print Statistics


class Timer:

    """Timer class
    Usage:
      t = Timer()
      # figure out how long it takes to do stuff...
      elapsed_s = t.elapsed_s() OR elapsed_min = t.elapsed_min()
    """

    def __init__(self):
        "Timer - Start a timer"
        self.s_per_min = 60.0  # Number seconds per minute
        self.start = time.time()

    def elapsed_s(self):
        "elapsed_s - Seconds elapsed since start (wall clock time)"
        return time.time() - self.start

    def elapsed_min(self):
        "elapsed_min - Minutes elapsed since start (wall clock time)"

        # Get elapsed seconds and convert to minutes
        return self.elapsed_s() / self.s_per_min


sample_set = 3
board_size = 8
search_algs = [BreadthFirst, DepthFirst, Manhattan]

debug_flag = False
# use to track loop invariant -> only set to false when something wrong in for loop
driver_flag = True
verbose_flag = False


def driver():
    plan_length = dict()  # use dict() to build key-value dictionaries
    num_nodes = dict()
    time_elapsed = dict()

    for alg in search_algs:
        # create key-lists in the dictionary for each search algorithm
        plan_length[alg] = list()
        num_nodes[alg] = list()
        time_elapsed[alg] = list()

    for sample in range(sample_set):
        # convert passed in board into a tuple
        print('Trial number #%d' % (sample+1))
        new_board = TileBoard(board_size).state_tuple()

        for alg in search_algs:
            if driver_flag is True:
                print('Algorithm used %s' % alg.__name__)

            # new_puzzle uses passed in g and h as heuristics
            new_puzzle = NPuzzle(board_size, g=alg.g,
                                 h=alg.h, force_state=new_board)
            start_timer = Timer()  # start timer for counting search duration
            # path taken by the search by respective searches
            path_taken = graph_search(
                new_puzzle, debug=debug_flag, verbose=verbose_flag)
            # track nodes that have been already explored
            nodes_explored = graph_search(
                new_puzzle, debug=debug_flag, verbose=verbose_flag)
            # time during particular search
            search_time = start_timer.elapsed_s()

            # add length of the tree
            plan_length[alg].append(len(path_taken))
            num_nodes[alg].append(nodes_explored)  # number of nodes expand
            time_elapsed[alg].append(search_time)  # time elapsed for alg

            if driver_flag is True:
                print('Puzzle solved with %s in %d time' %
                      (alg.__name__, search_time))

        print('Finished puzzle trial #%d' % (sample + 1))

    if driver_flag is True:
        print("\n\n################################\n\n\n")

    firstline = ["Algorithm ",
                 "Length of Plan (Mean,Standard Deviation)",
                 "Number of Nodes Expanded (Mean, Standard Deviation)"]
    rows = list()  # generate table by rows

    # vals
    for alg in search_algs:
        rows.append([' '.join(re.sub('(?!^)([A-Z][a-z]+)', r' \1', alg.__name__).split()),
                     '{:.3f} / {:.3f}'.format(
                         mean(length_of_plan[alg]), stdev(length_of_plan[alg])),
                     '{:.3f} / {:.3f}'.format(
                         mean(number_of_nodes[alg]), stdev(number_of_nodes[alg])),
                     '{:.3f} / {:.3f}'.format(mean(elapsed_time[alg]), stdev(elapsed_time[alg]))])

    print_vals(rows, firstline=firstline, sep="\t| ")


if __name__ == '__main__':
    driver()
