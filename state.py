# The definition of stage and the step function

import random


class State:
    def __init__(self, d=0, p=0):
        self.dealer = d
        self.player = p

    def initialize(self):
        self.dealer = random.randint(1, 10)
        self.player = random.randint(1, 10)


def draw():
    return (-1) ** random.randint(0, 2) * random.randint(1, 10)


def step(state, action):
    """
    :param state: the current state
    :param action: 1 for stick and 0 for hit
    :return: the next state and the reward
    """
    if action == 1:
        while state.dealer <= 16:
            state.dealer += draw()
            if state.dealer < 1:
                state.dealer = 0
                return state, 1
            if state.dealer > 21:
                state.dealer = 22
                return state, 1
        if state.dealer < state.player:
            reward = 1
        elif state.dealer == state.player:
            reward = 0
        else:
            reward = -1
        return state, reward
    else:
        state.player += draw()
        if state.player < 1:
            state.player = 0
            return state, -1
        if state.player > 21:
            state.player = 22
            return state, -1
        return state, 0
