import numpy as np
import sys

# This is the number of edges connected to each node in the DFA used for problem 1.
prob1_dfa_connections = np.array([[1, 2, 3], [3, 2, 1], [2,3,1]], dtype=object)




def prob1(n, test=False):
    '''
    Prompt for input then count the number of valid strings.
    '''
    if test:
        return count(n, generate_test_matrix())
    return count(n, prob1_dfa_connections)


def generate_test_matrix(m_x_m=100):
    '''
    return randomly generated matrix of size (m,m)
    '''
    # This is how you can generate a 100x100 of type objet
    # array randomly filled with 0-99 
    a = np.random.randint(100,size=(m_x_m, m_x_m))
    b = np.zeros([m_x_m, m_x_m], dtype='object')
    np.copyto(b, a, casting='unsafe')
    return b


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

    starting_states = np.ones([1,dfa_transition_count.shape[0]], dtype='object')
    ending_states = np.ones([dfa_transition_count.shape[1], 1], dtype='object')

    dfa_transition_count = pow(dfa_transition_count, n)
    

    print('shape1: ', str(starting_states.shape))
    print('shape2: ', str(dfa_transition_count.shape))
    print('shape3: ', str(ending_states.shape))
    return np.dot(np.dot(starting_states, dfa_transition_count),ending_states)

def pow(a,n):
    '''
    inputs:
    a : np array of shape (m,m)
    n : number to raise a to

    return the matrix a ^ n of shape (m,m)
    '''
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


if __name__== '__main__':
    argv1 = int(sys.argv[1])
    try:
        argv2 = bool(sys.argv[2])
        print(str(prob1(argv1, test=argv2)))
    except:
        print(str(prob1(argv1)))
          

          

