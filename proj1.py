import numpy as np
import sys
import time

# This is the number of edges connected to each node in the DFA used for problem 1.
prob1_dfa_connections = np.array([[1, 2, 3], [3, 2, 1], [2,3,1]], dtype=object)


def prob1(n, test=False):
    '''
    Prompt for input then count the number of valid strings.
    '''
    if test:
        a, b, c = generate_test_matrices(max_val=100, m=50)
        return count(n, a, b, c)[0][0]

    
    starting_states = np.ones([1,prob1_dfa_connections.shape[0]], dtype='object')

    ending_states = np.ones([prob1_dfa_connections.shape[1], 1], dtype='object')

    return count(n, starting_states,prob1_dfa_connections, ending_states)[0][0]


def count(n, starting_states, count_matrix, ending_states):
    '''
    Purpose : Compute the number of strings w of length n over {a, b, c}
    with the following property: In any substring of length 4 of w, all 3
    letters a,b,c occur.

    e.g. 
    abbcaabca is valid as {a,b,c} all appear in every 4 digit substring

    aabbcabac is not valid since {a,b,c} don't all exists in the 4 char 
    string aabb
    '''

    dfa_transition_count = np.linalg.matrix_power(count_matrix,n)
    return np.dot(np.dot(starting_states, dfa_transition_count),ending_states)



def generate_test_matrices(max_val, m):
    '''
    return:
    a = [1,m] matrix of 0 and 1's
    b = [m,m]
    c = [m,1]
    '''
    a = generate_test_matrix(shape=(1,m), max_val=2) 
    b = generate_test_matrix(shape=(m,m), max_val=max_val)
    c = generate_test_matrix(shape=(m,1), max_val=2)

    return a,b,c



def generate_test_matrix(shape, max_val=100):
    '''
    return randomly generated matrix of size (m,m)
    '''
    # This is how you can generate a 100x100 of type objet
    # array randomly filled with 0-99 
    a = np.random.randint(max_val,size=shape)
    b = np.zeros([a.shape[0], a.shape[1]], dtype='object')
    np.copyto(b, a, casting='unsafe')
    return b







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
    start = time.time()
    try:
        argv2 = bool(sys.argv[2])
        ret_val = str(prob1(argv1, test=argv2))
        print(ret_val)
        print('len of solution: ', len(ret_val))
        
    except:
        print(str(prob1(argv1)))

    print('total time elapsed: ', str(time.time()-start), ' seconds')
          

          

