#Ran Ju 1621899
#CSE 415, Assignment 3, Part 2
#Problem3: A-star algorithm implementation

# Astar.py, April 2017
# Based on ItrDFS.py, Ver 0.4a, October 14, 2017.

# A* Search of a problem space.
# The Problem should be given in a separate Python
# file using the "QUIET" file format.
# See the TowerOfHanoi.py example file for details.
# Examples of Usage:

# A small change was made on Oct. 14, so that backtrace
# uses None as the BACKLINK value for the initial state,
# just as in ItrDFS.py, rather than using -1 as it did
# in an earlier version.

# python3 AStar.py EightPuzzleWithHeuristics h_manhattan

import sys
from priorityq import PriorityQ

# DO NOT CHANGE THIS SECTION 
if sys.argv == [''] or len(sys.argv) < 2:
    import EightPuzzleWithHeuristics as Problem
    heuristics = lambda s: Problem.HEURISTICS['h_euclidean'](s)

else:
    import importlib
    Problem = importlib.import_module(sys.argv[1])
    heuristics = lambda s: Problem.HEURISTICS[sys.argv[2]](s)

print("\nWelcome to AStar")
COUNT = None
BACKLINKS = {}


# DO NOT CHANGE THIS SECTION
def runAStar():
    # initial_state = Problem.CREATE_INITIAL_STATE(keyVal)
    initial_state = Problem.CREATE_INITIAL_STATE()
    print("Initial State:")
    print(initial_state)
    global COUNT, BACKLINKS
    COUNT = 0
    BACKLINKS = {}
    path, name = AStar(initial_state)
    print(str(COUNT) + " states examined.")
    return path, name


# A star search algorithm
# TODO: finish A star implementation
def AStar(initial_state):
    global COUNT, BACKLINKS
    # TODO: initialze and put first state into
    # priority queue with respective priority
    # add any auxiliary data structures as needed
    OPEN = PriorityQ()
    CLOSED = []
    #define the g score which means
    #the cost of the move will increase by 1 at each depth
    g = {}
    g[initial_state]  = 0
    BACKLINKS[initial_state] = None
    #in priority queue, the state is the element
    #and the F score is the priority
    #F socre is the heuristics score plus g scorce
    OPEN.insert(initial_state, g[initial_state] + 0)

    while not OPEN.isEmpty():
        COUNT += 1
        S = OPEN.deletemin()
        while S in CLOSED:
            S = OPEN.deletemin()
        CLOSED.append(S)
        # DO NOT CHANGE THIS SECTION: begining
        if Problem.GOAL_TEST(S):
            print(Problem.GOAL_MESSAGE_FUNCTION(S))
            path = backtrace(S)
            return path, Problem.PROBLEM_NAME
            # DO NOT CHANGE THIS SECTION: end

            # TODO: finish A* implementation
        for op in Problem.OPERATORS:
            if op.precond(S):
                new_state = op.state_transf(S)
                if not (new_state in CLOSED):
                    h = heuristics(new_state)
                    g[new_state] = g[S] + 1
                    if new_state not in OPEN:
                        OPEN.insert(new_state, h + g[new_state])
                        BACKLINKS[new_state] = S


# DO NOT CHANGE
def backtrace(S):
    global BACKLINKS
    path = []
    while S:
        path.append(S)
        S = BACKLINKS[S]
    path.reverse()
    print("Solution path: ")
    for s in path:
        print(s)
    print("\nPath length = " + str(len(path) - 1))
    return path


if __name__ == '__main__':
    path, name = runAStar()


