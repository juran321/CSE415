#Ran Ju 1621899
#CSE 415 HW3 Part2
#Problem4: Implement and Comparing Heuristics

import math
# <METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Eight Puzzle Heuristics"
PROBLEM_VERSION = "0.2"
PROBLEM_AUTHORS = ['R. Ju']
PROBLEM_CREATION_DATE = "18-OCT-2017"
PROBLEM_DESC = \
    '''This formulation of the Eight Puzzle problem with Heuristics like hamming distance uses generic
    Python 3 constructs and has been tested with Python 3.6.
    It is designed to work according to the QUIET2 tools interface.
    '''


# </METADATA>

# <COMMON_CODE>
class State():
    def __init__(self, d):
        self.d = d

    def __str__(self):
        # Produces a brief textual description of a state.
        d = self.d
        txt = str(d)
        return txt

    def __eq__(self, s2):
        if not (type(self) == type(s2)): return False
        d1 = self.d
        d2 = s2.d
        return d1 == d2

    def __hash__(self):
        return (str(self)).__hash__()

    def __copy__(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State([])
        for num in self.d:
            news.d.append(num)
        return news

    def can_move(self, From, To):
        '''Testes whether it's legal to move a tile in a given position
        to another given position'''
        try:
            pos = GOAL_STATE
            state = self.d
            if(From == To):
                return False
            if self.d[From] == 0 or self.d[To] != 0:
                return False
            if From not in pos or To not in pos:
                return False
            if To in step[From]:
                return True
            return False  # all other conditions cannot move
        except (Exception) as e:
            print(e)

    def move(self, From, To):
        '''Assuming it is legal to make the move, this computes the
        new state resulting from moving a tile(From) to other tile(To)'''
        news = self.__copy__()  # start with a deep copy
        d2 = news.d
        d2[To] = d2[From]
        d2[From] = 0# replace target number with 0
        return news



def goal_test(s):
    '''If the list is [0,1,2,3,4,5,6,7,8], then s is a goal state.'''
    return s.d == GOAL_STATE


def goal_message(s):
    return "The Basic Eight Puzzle Transport is Triumphant!"


class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)


# </COMMON_CODE>
def posX(x, y):
    return x % 3 - y % 3
def posY(x,y):
    return int (x / 3) - int(y / 3)


def h_euclidean(state):
  distances = []
  for i,v in enumerate(state.d):
    dist = math.sqrt((posY(i, v))**2 + (posX(i, v))**2)
    distances.append(dist)
  return sum(distances)

def h_manhattan(state):
  distances = []
  for i,v in enumerate(state.d):
    dist = abs(posX(i,v)) + abs(posY(i,v))
    distances.append(dist)
  return sum(distances)

def h_hamming(state):
  distance = 0
  for i,v in enumerate(state.d):
    if GOAL_STATE[i] != v:
        distance += 1
  return distance

def h_custom(state):
  h1 = h_manhattan(state)
  h2 = h_euclidean(state)
  h3 = h_hamming(state)
  return max(h1,h2,h3)

# <COMMON_DATA>
GOAL_STATE = [0,1,2,3,4,5,6,7,8]
# </COMMON_DATA>
#this dict contain each position in the 8 puzzle can move which position of tile
step = {0: [1, 3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[6,4,8],8:[5,7]}

# <INITIAL_STATE>
# INITIAL_STATE = State([1,4,2,3,7,0,6,8,5])
# CREATE_INITIAL_STATE = lambda : INITIAL_STATE
# puzzle0:
#CREATE_INITIAL_STATE = lambda: State([0, 1, 2, 3, 4, 5, 6, 7, 8])
# puzzle1a:
#CREATE_INITIAL_STATE = lambda: State([1, 0, 2, 3, 4, 5, 6, 7, 8])
# puzzle2a:
#CREATE_INITIAL_STATE = lambda: State([3, 1, 2, 4, 0, 5, 6, 7, 8])
# puzzle4a:
#CREATE_INITIAL_STATE = lambda: State([1, 4, 2, 3, 7, 0, 6, 8, 5])
#puzzle10a.py:
#CREATE_INITIAL_STATE = lambda: State([4, 5, 0, 1, 2, 3, 6, 7, 8])

#puzzle12a.py:
#CREATE_INITIAL_STATE = lambda: State([3, 1, 2, 6, 8, 7, 5, 4, 0])

#puzzle14a.py:
#CREATE_INITIAL_STATE = lambda: State([4, 5, 0, 1, 2, 8, 3, 7, 6])

#puzzle16a.py:
CREATE_INITIAL_STATE = lambda: State([0, 8, 2, 1, 7, 4, 3, 6, 5])
# </INITIAL_STATE>

# <OPERATORS>
from itertools import product
tiles = product(range(9), range(9))


OPERATORS = [Operator("Move the tile from " + str(p) + " to ",

                      lambda s,p1=p: s.can_move(p1,q1),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s,p1=p,q1=q: s.move(p1,q1))
             for (p, q) in tiles]

# </OPERATORS>

# <GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>

#<HEURISTICS> (optional)
HEURISTICS = {'h_hamming': h_hamming,'h_manhattan': h_manhattan, 'h_euclidean': h_euclidean, 'h_custom': h_custom}
#</HEURISTICS>