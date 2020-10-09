# Training in Q-learning

from state import *

QTable = [[0, 0] for _ in range(21*10)]    # 21*10 states and 2 actions
alpha = 0.5    # learning rate
epsilon = 1    # exploration parameter


def update(state, a, e):
    st = state.player - 1
    explore = random.random()
    if explore >= e:
        action = 0 if QTable[st][0] > QTable[st][1] else 1
    else:
        action = random.randint(0, 1)
    next_state, reward = step(state, action)
    nextQ = max(QTable[next_state.player - 1])
    QTable[st][action] += a * (reward + nextQ - QTable[st][action])
