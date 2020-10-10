# Training in Q-learning

from state import *
import numpy as np

QTable = np.zeros((21 * 10, 2))    # 21*10 states and 2 actions
alpha = 0.01    # learning rate
epsilon = 1     # exploration parameter


def update(state, a, e):
    d = state.dealer - 1
    while 1 <= state.dealer <= 10 and 1 <= state.player <= 21:
        st = 21 * d + state.player - 1
        explore = random.random()    # epsilon-greedy
        if explore >= e:
            action = 0 if QTable[st][0] >= QTable[st][1] else 1
        else:
            action = random.randint(0, 1)
        next_state, reward = step(state, action)
        if 1 <= next_state.dealer <= 10 and 1 <= next_state.player <= 21:
            nextQ = max(QTable[21 * d + next_state.player - 1])
        else:
            nextQ = reward
        QTable[st][action] += a * (reward + nextQ - QTable[st][action])


for i in range(200000):
    update(State(), alpha, epsilon)
    epsilon *= 0.99
    # alpha *= 0.99


if __name__ == '__main__':
    print(QTable)
