# Harjot Singh CSC 158 ASSIGNMENT 1
# [ MLEFT, CLEFT, BOAT, MRIGHT, CRIGHT, DEPTH, [ ACTION ], [ PARENT ] ]
initialState = [3, 3, 0, 0, 0, 0]
arrfringe = []
closedarr = []
goalState = [0, 0, 1, 3, 3]
TempArr = []
actionFORWARDarr = [ (-2,0,2,0) , (-1,-1,1,1) , (0,-2,0,2) , (-1,0,1,0) , (0,-1,0,1) ]
actionBACKWARDarr = [ (2,0,-2,0) , (1,1,-1,-1) , (0,2,0,-2) , (1,0,-1,0) , (0,1,0,-1) ]
def checkifInfinLoop(state):
    if(state[0] == 3 and state[1] == 3):
        return True
    else:
        return False

# function checks if a state is valid or not
def checkValid(state):
    if( (state[0] < 0) or (state[1] < 0) or (state[3] < 0) or (state[4] < 0) or (checkifInfinLoop(state) == True) ):
        return False
    elif((state[0] == 0 or state[0] >= state[1]) and (state[3] == 0 or state[3] >= state[4])):
        return True
    else:
        return False

# function finds a new state depending on a action and a state
def findnewState(action, state):
    newState = []
    newState.append(state[0]+action[0])
    newState.append(state[1]+action[1])

    if(state[2] == 0):
        newState.append(1)
    else:
        newState.append(0)
    
    newState.append(state[3]+action[2])
    newState.append(state[4]+action[3])

    newState.append(state[5]+1)

    # newState.append(action)
    # newState.append(state)

    return newState

# function finds all possible actions from one state
def actions(state):
    AllOptions = []
    if(state[2] == 0):
        for oneaction in actionFORWARDarr:
            AllOptions.append(findnewState(oneaction, state))
    else:
        for oneaction in actionBACKWARDarr:
            AllOptions.append(findnewState(oneaction, state))    
    for aState in AllOptions:
        if(checkValid(aState) == True):
            arrfringe.append(aState)

def checkforSolution(state):
    if(state[0] == goalState[0]):
        if(state[1] == goalState[1]):
            if(state[2] == goalState[2]):
                if(state[3] == goalState[3]):
                    if(state[4] == goalState[4]):
                        return True
                    else:
                        return False
                else:
                    return False    
            else:
                return False
        else:
            return False
    else:
        return False


# Main function to find solution
def BFS():
    arrfringe.append(initialState) # adding start state to fringe
    while(True):
        currentState = arrfringe.pop(0) # first in first out
        closedarr.append(currentState)
        if(checkforSolution(currentState) == True):
            print("CURRENT STATE FOUND: " + ("depth = " + str(currentState[5]) + " Current State: " + str(currentState)))
            print("Number of Visited Nodes = " + str(len(closedarr)))
            print("Number of UnVisited Nodes = " + str(len(arrfringe)))
            return currentState
        else:
            #print("depth = " + str(currentState[5]) + " Current State: " + str(currentState))
            actions(currentState) # add all new found states to the fringe


BFS()
