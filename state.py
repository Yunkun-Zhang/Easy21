# The definition of stage and the step function

import random


class State:
    def __init__(self):
        self.dealer = random.randint(1, 10)
        self.player = random.randint(1, 10)


def draw():
    return (-1) ** random.randint(0, 2) * random.randint(1, 10)


def step(state, action):
    """

    :param state: the current state
    :param action: True for stick and False for hit
    :return: the next state and the reward
    """
    if action:
        while state.dealer <= 16:
            state.dealer += draw()
            if state.dealer < 1:
                state.dealer = 0
                return state, 1
            if state.dealer > 21:
                state.dealer = 22
                return state, 1
        reward = 1 if state.dealer < state.player else 0 if state.dealer == state.player else -1
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
