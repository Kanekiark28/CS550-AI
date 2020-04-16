"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles with a single solution
    where the blank is at the bottom right, e.g.:
        123
        456
        78
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""

import math
from basicsearch_lib02.searchrep import Node
from basicsearch_lib02.tileboard import TileBoard
# For each of the following classes, create classmethods g and h
# with the following signatures
#       @classmethod
#       def g(cls, parentnode, action, childnode):
#               return appropritate g value
#       @classmethod
#        def h(cls, state):
#               return appropriate h value


class BreadthFirst:
    "BredthFirst - breadthfirst search"
    constant = 1

    @classmethod
    def g(cls, parentnode: Node, action, childnode: Node):
        # goal depth
        return len(childnode.path())

    @classmethod
    def h(cls, state: TileBoard):
        return cls.constant


class DepthFirst:
    "DepthFirst - depth first search"
    @classmethod
    def g(cls, parentnode: Node, action, childnode: Node):
        return (parentnode.depth + 1) * -1

    @classmethod
    def h(cls, state: TileBoard):
        return 0


class Manhattan:
    "Manhattan Block Distance heuristic"
    @classmethod
    def g(cls, parentnode, action, childnode: Node):
        return childnode.depth * 2

    @classmethod
    def h(cls, state: TileBoard):
        manhattan_val = 0

        solved_states = [[None for c in range(
            state.cols)] for r in range(state.rows)]

        idx = 1
        for row in range(state.boardsize):
            for col in range(state.boardsize):
                if row == state.rows // 2 and col == state.cols // 2:
                    solved_states[row][col] = None
                else:
                    solved_states[row][col] = idx
                    idx += 1

        for row in range(state.boardsize):
            for col in range(state.boardsize):
                key = state.get(row, col)
                for r in range(len(solved_states)):
                    if key in solved_states[r]:
                        manhattan_val += abs(r - row) + \
                            abs(solved_states[r].index(key)-col)
        return manhattan_val
