#Ran Ju 1621899
#CSE 415 HW3 Part2
#Problem2: 8 Puzzle Formulation

# <METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Basic Eight Puzzle"
PROBLEM_VERSION = "0.2"
PROBLEM_AUTHORS = ['R. Ju']
PROBLEM_CREATION_DATE = "18-OCT-2017"
PROBLEM_DESC = \
    '''This formulation of the Basic Eight Puzzle problem uses generic
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
        txt = str(self.d)
        return txt

    def __eq__(self, s2):
        if not (type(self) == type(s2)): return False
        return self.d == s2.d

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
            return False

        except (Exception) as e:
            print(e)

    def move(self, From, To):
        '''Assuming it is legal to make the move, this computes the
        new state resulting from moving a tile(From) to other tile(To)'''
        news = self.__copy__()  # start with a deep copy
        d2 = news.d
        d2[To] = d2[From]
        d2[From] = 0
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

# <COMMON_DATA>
GOAL_STATE = [0,1,2,3,4,5,6,7,8]
# </COMMON_DATA>
#this dict contain each position in the 8 puzzle can move which position of tile
step = {0: [1, 3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[6,4,8],8:[5,7]}

# <INITIAL_STATE>
INITIAL_STATE = State([1,4,2,3,7,0,6,8,5])
CREATE_INITIAL_STATE = lambda : INITIAL_STATE
# puzzle0:
#CREATE_INITIAL_STATE = lambda: State([0, 1, 2, 3, 4, 5, 6, 7, 8])
# puzzle1a:
#CREATE_INITIAL_STATE = lambda: State([1, 0, 2, 3, 4, 5, 6, 7, 8])
# puzzle2a:
#CREATE_INITIAL_STATE = lambda: State([3, 1, 2, 4, 0, 5, 6, 7, 8])
# puzzle4a:
#CREATE_INITIAL_STATE = lambda: State([1, 4, 2, 3, 7, 0, 6, 8, 5])
# </INITIAL_STATE>

# <OPERATORS>
from itertools import product
tiles = product(range(9), range(9))

distance_combinations = [1, -1, 3,-3]
OPERATORS = [Operator("Move the tile from " + str(p) + " to ",

                      lambda s,p1=p,q1=q: s.can_move(p1,q1),
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
