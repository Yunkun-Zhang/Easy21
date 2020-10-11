# Training in Q-learning

from state import *
import numpy as np
from tqdm import tqdm

QTable = np.zeros((21 * 10, 2))  # 21*10 states and 2 actions
alpha = 0.01  # learning rate
epsilon = 1  # exploration parameter


def update(state, a, e):
    while 1 <= state.dealer <= 10 and 1 <= state.player <= 21:  # 合法状态
        d = state.dealer - 1
        st = 21 * d + state.player - 1
        explore = random.random()  # epsilon-greedy
        if explore >= e:  # 根据当前策略行进
            action = 0 if QTable[st][0] >= QTable[st][1] else 1
        else:  # 随机游走
            action = random.randint(0, 1)
        next_state, reward = step(state, action)
        if 1 <= next_state.dealer <= 10 and 1 <= next_state.player <= 21:
            d=next_state.dealer-1
            nextQ = max(QTable[21 * d + next_state.player - 1])
        else:
            nextQ = reward
        QTable[st][action] += a * (reward + nextQ - QTable[st][action])


print("Training in Q-learning ......")
for i in range(200000):
    s=State()
    s.initilize()
    update(s, alpha, epsilon)
    epsilon *= 0.99
    # alpha *= 0.99

if __name__ == '__main__':
    print(QTable)
