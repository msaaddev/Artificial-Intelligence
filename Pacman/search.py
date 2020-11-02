# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def DFS(problem):
    """
    Challenge #1

    Reasons why the pacman is getting stuck:
        It is because there comes a point where when the getSucessor function is called, the first successor in the successor array is the path to the previous state where the pacman is coming from. So it moves down. And at that stage, when the pacman goes down and the getSucessor function is called again, the the first successor is the above path. This process repeats again and again.

        The problem lies in children = problem.getSuccessors(currentState)
     """

    """ Challenge #2 """
    # util.raiseNotDefined()
    currentState = problem.getStartState()
    actions = []
    maxIterations = 20
    prevState = ""
    while(maxIterations >= 0):
        children = problem.getSuccessors(currentState)
        if (prevState == "West" and getActionFromTriplet(children[0]) == "East") or (prevState == "South" and getActionFromTriplet(children[0]) == "North") or (prevState == "East" and getActionFromTriplet(children[0]) == "West") or (prevState == "North" and getActionFromTriplet(children[0]) == "South"):
            actions.append(getActionFromTriplet(children[1]))
            prevState = getActionFromTriplet(children[1])
            firstChild = children[1]
        else:
            actions.append(getActionFromTriplet(children[0]))
            prevState = getActionFromTriplet(children[0])
            firstChild = children[0]
        firstChildState = firstChild[0]
        currentState = firstChildState
        maxIterations = maxIterations - 1
    return actions


def depthFirstSearch(problem):
    frontier = util.Stack()
    frontier.push((problem.getStartState(), []))
    explored = [problem.getStartState()]

    while frontier.isEmpty() == 0:
        state, actions = frontier.pop()
        explored.append(state)

        for newState in problem.getSuccessors(state):
            newStateValue = newState[0]
            newStateDirection = newState[1]
            if newStateValue not in explored:
                if problem.isGoalState(newStateValue):
                    return actions + [newStateDirection]
                else:
                    frontier.push(
                        (newStateValue, actions + [newStateDirection]))
                    explored.append(newStateValue)
    util.raiseNotDefined()


def getActionFromTriplet(triple):
    return triple[1]


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def mediumClassicSearch(problem):
    from game import Directions
    w = Directions.WEST
    return [w, w]


def mediumMazeSearch(problem):
    from game import Directions
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    s = Directions.SOUTH
    return [w, w, w, w, w, w, w, w, w,
            s, s, e, e, s, s, s, w, w,
            w, n, w, w, w, w, s, s, s,
            e, e, e, e, e, e, e, s, s,
            s, s, s, s, s, w, w, w, w,
            w, w, w, w, w, w, w, w, w,
            w, w, w, w, s, w, w, w, w,
            w, w, w, w, w]


def bigMazeSearch(problem):
    from game import Directions
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    s = Directions.SOUTH
    return [n, n, w, w, w, w, n, n, w,
            w, s, s, w, w, w, w, w, w,
            w, w, w, w, w, w, w, w, n,
            n, e, e, n, n, w, w, n, n,
            n, n, n, n, e, e, e, e, e,
            e, s, s, e, e, n, n, e, e,
            e, e, n, n, e, e, s, s, e,
            e, n, n, n, n, n, n, e, e,
            e, e, n, n, n, n, n, n, n,
            n, n, n, w, w, s, s, w, w,
            w, w, s, s, s, s, s, s, w,
            w, s, s, s, s, w, w, n, n,
            w, w, w, w, w, w, w, w, w,
            w, w, w, n, n, e, e, n, n,
            n, n, n, n, e, e, e, e, e,
            e, n, n, n, n, n, n, n, n,
            w, w, w, w, w, w, s, s, w,
            w, w, w, s, s, s, s, e, e,
            s, s, w, w, w, w, w, w, w,
            w, w, w, s, s, s, s, s, s,
            s, s, s, s, e, e, s, s, s,
            s, w, w, s, s, s, s, e, e,
            s, s, w, w, s, s, s, s, w,
            w, s, s]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
