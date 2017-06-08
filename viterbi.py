# -*- coding: utf-8 -*-
'''
author:yangyl

'''
# Code from the wikipedia page for Viterbi algorithm done or modified by Zhubarb
# More implementations of Viterbi algorithm can be found at http://stackoverflow.com/questions/9729968/python-implementation-of-viterbi-algorithm
# Example of implementation of the viterbi algorithm for a  primitive clinic in a village.
# People in the village have a very nice property that they are either healthy or have a fever.
# They can only tell if they have a fever by asking a doctor in the clinic.
# The wise doctor makes a diagnosis of fever by asking patients how they feel.
# Villagers only answer that they feel normal, dizzy, or cold.

states = ('Healthy', 'Fever')

observations = ('normal', 'normal', 'dizzy','cold')

start_probability = {'Healthy': 0.6, 'Fever': 0.4}

transition_probability = {
    'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
    'Fever': {'Healthy': 0.4, 'Fever': 0.6}
}

emission_probability = {
    'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
}


# Helps visualize the steps of Viterbi.
def print_dptable(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            # argmax {V[t-1][i]*trans_p[i][j]}* emit_p[j][obs[t]]
            (prob, state) = max((V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        # Don't need to remember the old paths
        path = newpath
    print 'V...',V
    print_dptable(V)
    (prob, state) = max((V[t][y], y) for y in states)
    return (prob, path[state])


def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)

V = [{}]
V[0][0]=1
V.append({})
V[1]={3:7}
print V
print V[0]
print V[1]
print(example())