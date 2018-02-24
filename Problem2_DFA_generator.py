import numpy as np


class DFA:
    current_state = None

    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return

    def transition_to_state_with_input(self, input_value):
        if (self.current_state, input_value) not in self.transition_function.keys():
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return

    def in_accept_state(self):
        return self.current_state in self.accept_states

    def go_to_initial_state(self):
        self.current_state = self.start_state
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
        return self.in_accept_state()

    def breadth_first_search(self, vertex):
        reach = np.zeros(len(self.states))
        parent = len(self.states) * [None]
        q = [vertex]
        while(len(q)>0):
            x = q.pop(0)
            for elem in self.alphabet:
                index = self.transition_function[x,elem]
                if reach[index] == 0: 
                    reach[index] = 1
                    parent[index] = [x, elem]
                    q.append(index)
                    if index in self.accept_states:
                        return reach,parent
        return reach,parent

    def find_int(self, parents, reach):
        path = []
        if reach[0] == 0:
            return None
        current = 0
        while parents[current][0] != 0:
            if reach[current] != 0:
                path.append(parents[current][1])
                current = parents[current][0]
            else:
               break
        path.append(parents[current][1])
        path.reverse()
        return(path)        


def gen_dfa(k, alphabet):
    states = set()
    for i in range(k):
        states.add(i)

    for i in range(len(alphabet)):
        alphabet[i] = int(alphabet[i])

    tf = dict()
    for current_state in states:
        for letter in alphabet:
            tf[current_state, letter] = (10*current_state+letter) % k

    accept_states = {0}
    start_state = 0
    d = DFA(states, alphabet, tf, start_state, accept_states)


    return d


def min_string(u_input, alphabet):
    """
    input:
       u_input: the user input number

    """
    if ("0" in alphabet) and len(alphabet) == 1:
        return None
    d = gen_dfa(u_input, alphabet)
    reach, parents = d.breadth_first_search(0)
    num_array = d.find_int(parents, reach)
    str_val = ""
    for elem in num_array:
        str_val+=str(elem)
    return str_val


