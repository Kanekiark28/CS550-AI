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

#Create 31 Trials
#For each Trial, Use BFS, DFS, A* using Manhattan Distance
#Keep track of the nodes expanded through -> Frontier set? and amount of time
#Print Statistics

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

sample_set = 2 
board_size = 8
search_algs = [BreadthFirst,DepthFirst,Manhattan]
debug_flag = False
info_flag = True
verbose_flag = False
    
def driver() :
    plan_length = dict()
    num_nodes = dict()
    time_elapsed = dict()

    for alg in search_algs:
        #create key lists in the dictionary
        planlen[searchalgs] = list()
        numnodes[searchalgs] = list()
        timeelapsed[searchalgs] = list()

    for s in range(sample):
        # if info_flag:
        #   print('Starting at" % (s+1))

        newboard = TileBoard(sample).state_tuple()

        for alg in searchalgs:
            if info_flag:
                print('Algorithm used %s' %alg.__name__) 
            
            newpuzzle = NPuzzle(sample, g=method.g, h=method.h, force_state=newboard)

            start_timer = self.start
            goalpath = graph_search(puzzle, debug = debug_flag, verbose= verbose)
            nodes_explored = graph_search(puzzle, debug = debug_flag, verbose= verbose)
            time_elapsed = elapsed_s(start_timer)

         


if __name__ == '__main__':
    driver()
