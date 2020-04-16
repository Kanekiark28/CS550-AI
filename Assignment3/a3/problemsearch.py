'''
problemsearch - Functions for seaarching.
'''

from basicsearch_lib02.searchrep import (Node, Problem, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from explored import Explored
from collections import deque


def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.

    If debug is True, debugging information will be displayed.

    if verbose is True, the following information will be displayed:

        Number of moves to solution
        List of moves and resulting puzzle states
        Example:

            Solution in 25 moves
            Initial state
                  0        1        2
            0     4        8        7
            1     5        .        2
            2     3        6        1
            Move 1 -  [0, -1]
                  0        1        2
            0     4        8        7
            1     .        5        2
            2     3        6        1
            Move 2 -  [1, 0]
                  0        1        2
            0     4        8        7
            1     3        5        2
            2     .        6        1

            ... more moves ...

                  0        1        2
            0     1        3        5
            1     4        2        .
            2     6        7        8
            Move 22 -  [-1, 0]
                  0        1        2
            0     1        3        .
            1     4        2        5
            2     6        7        8
            Move 23 -  [0, -1]
                  0        1        2
            0     1        .        3
            1     4        2        5
            2     6        7        8
            Move 24 -  [1, 0]
                  0        1        2
            0     1        2        3
            1     4        .        5
            2     6        7        8

        If no solution were found (not possible with the puzzles we
        are using), we would display:

            No solution found

    Returns a tuple (path, nodes_explored) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    """
    frontier_set = PriorityQueue()  # frontier set for the end of all visited paths
    # add initial problem to the frontier set
    frontier_set.append(Node(problem, problem.initial))
    curr_node = frontier_set.pop()  # current node for exploration
    # explore the node through searchalgs
    search_flag = True
    if curr_node.expand(curr_node.problem)[0].g < 0:
            # Depth first
        frontier_set = deque()  # initialize left to right deque
        frontier_set.append(Node(problem, problem.initial))
    elif curr_node.expand(curr_node.problem)[0].h < 2:
            # Breadth first
        search_flag = False  # Search flag to dictate through the BFS or DFS
        frontier_set = deque()
        frontier_set.append(Node(problem, problem.initial))
    else:
            # Manhattan
        frontier_set.append(Node)
    hash_frontier = Explored()  # add curr_node to the explored set
    hash_frontier.add(problem.initial.state_tuple())
    complete = False
    nodes_explored = 0
    explored = Explored()
    while not complete:
        if search_flag is not False:
            curr_node = frontier_set.pop()
        else:
            curr_node = frontier_set.popleft()

        if debug:
            print("Popping Node:", str(curr_node))

        explored.add(curr_node.state.state_tuple())
        nodes_explored += 1

        if curr_node.state.solved():
            if debug:
                print("Solution was found")
            goal_path = curr_node.path()
            solution_found = True
            if verbose:
                print(goal_path)
            return goal_path, nodes_explored
        else:
            for element in curr_node.expand(curr_node.problem):
                    # add elements to the frontier set
                    # if already not explored
                if not explored.exists(element.state.state_tuple()) and not hash_frontier.exists(element.state.state_tuple()):
                    frontier_set.append(element)
                    hash_frontier.add(element)
            complete = len(frontier_set) == 0
            if verbose:
                print("No Solution, please try a different puzzle!")
            return None, nodes_explored


def print_vals(input: tuple):
    print("Number of %d moves" % (len(input) - 1))
    pring("Initial state")
    print(input[0])

    for i in range(1, len(inpu)):
        print("Move %d - %s" % (i, input[i].action))
        print(input[i].state)
        print("")
