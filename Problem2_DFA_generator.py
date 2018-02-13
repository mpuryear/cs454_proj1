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
    pass


def test_dfa():
    # states = {0, 1, 2, 3}
    states = set()
    u_input = int(input("Enter a starting number: "))
    for i in range(u_input):
        states.add(i)

    # alphabet = {'a', 'b', 'c', 'd'}
    alphabet = input("which characters are allowed: ").split()
    for i in range(len(alphabet)):
        alphabet[i] = int(alphabet[i])

    tf = dict()
    for current_state in states:
        for letter in alphabet:
            tf[current_state, letter] = (10*current_state+letter) % u_input

    accept_states = {0}
    start_state = 0
    d = DFA(states, alphabet, tf, start_state, accept_states)

    inp_program = [1,1,1,1,1,1,1,1,1]

    print(d.run_with_input_list(inp_program))



if __name__ == "__main__":
    test_dfa()



