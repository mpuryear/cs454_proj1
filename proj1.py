import numpy as np
import sys
import time

# This is the number of edges connected to each node in the DFA used for problem 1.
transition_matrix = np.array(
    [[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
     [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]],
    dtype=object)


def prob1(n, test=False, verbose=False):
    '''
    Prompt for input then count the number of valid strings.
    '''
    if test:
        a, b, c = generate_test_matrices(max_val=100, m=50)
        return count(n, a, b, c)[0][0]

    
    starting_states = np.array(
        [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        , dtype='object')

    ending_states = np.array([[0],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [1],
                              [0]],
                             dtype='object')

    if(verbose):
        print("shape start_states: " , str(starting_states.shape))
        print("transition_matrix shape: ", str(transition_matrix.shape))
        print("shape ending_states: ", str(ending_states.shape))

   
    
    return count(n, starting_states, transition_matrix, ending_states)[0][0]


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







def prob2(k, digits):
    '''
    eg delta func :
    for n = input: k=26147 on the provided paper
    delta(i, j):  // returns next state, i is current state, j is next input
    return (10*i + j)%n


    must use bfs for something
    '''
    
    return 0

def test_prob1(n, expected):
    ret_val = prob1(n)
    print("\ntest input: ", str(n))
    print("output: ", str(ret_val))
    print("expected: ", str(expected))
    print("output == expected: ", str(expected == ret_val))

    
def test_prob2(k, digits, expected):
    ret_val = prob2(k, digits)
    print("\ntest input: ", str(k), ", ",  str(digits))
    if(expected == 1113313113):
        print("output: ", str(ret_val))
        print("expected: ", str(expected))
        print("output == expected", str(ret_val == expected))
    else:
        print("len(output) == len(expected)", str(len(str(ret_val)) == expected))
        

def handle_prob1():
    n = input('\n(prob1) input n: ')
    ret_val = prob1(int(n))
    print('\tn = ', n)
    print('\tnumber of strings of length n is : ', str(ret_val), "\n")
    return

def handle_prob2():
    k = input('\n(prob2) input k: ')
    digits = {}
    digits = input('(prob2)  input Digits permitted: ')
    print('\tInput: k = ', k, ', Digits permitted: ', str(digits))
    ret_val = prob2(k, digits)
    print('\tShortest multiple of k using digits {', digits, '}: ', str(ret_val))
    return
    
if __name__== '__main__':

    try:
        argv1 = bool(sys.argv[1]) # check for passed test param
        n = 137
        test_expected = 6119266976149912241614898841866546736
        test_prob1(n, test_expected)

        n = 100
        test_expected = 987802207638178400131884900
        test_prob1(n, test_expected)

        k = 26147
        digits = {1, 3}
        test_expected = 1113313113
        test_prob2(k, digits, test_expected)

        k = 198217
        digits = {1}
        test_expected_length = 10962
        test_prob2(k, digits, test_expected_length)
        
    except:

        while(True):
            user_input = input('Problem 1,2, or quit. (1,2,q) ')
            if user_input == '1':
                handle_prob1()
            elif user_input == '2':
                handle_prob2()
            else:
                break
            
          

          

