import numpy as np

prob1_dfa = np.array([[1, 2], [2, 1]])

def prob1():
    '''
    Prompt for input then count the number of valid strings.
    '''

    
    
    return count(100, prob1_dfa)


def count(n, dfa_transition_count):
    '''
    Purpose : Compute the number of strings w of length n over {a, b, c}
    with the following property: In any substring of length 4 of w, all 3
    letters a,b,c occur.

    e.g. 
    abbcaabca is valid as {a,b,c} all appear in every 4 digit substring

    aabbcabac is not valid since {a,b,c} don't all exists in the 4 char 
    string aabb
    '''

    starting_states = [1, 0]
    ending_states = np.array([[0], [1]])

    dfa_transition_count = pow(dfa_transition_count, n)
    
    return starting_states * dfa_transition_count * ending_states

def pow(a,n):
    return np.linalg.matrix_power(a,n)

def prob2():
    '''
    eg delta func :
    for n = input: k=26147 on the provided paper
    delta(i, j):  // returns next state, i is current state, j is next input
    return (10*i + j)%n


    must use bfs for something
    '''
    
    return


print(str(pow(prob1_dfa ,2)))


