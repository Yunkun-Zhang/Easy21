# Training in Q-learning

from state import *
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

QTable = np.zeros((10, 21, 2))  # 21*10 states and 2 actions
alpha = 0.5  # init learning rate
epsilon = 1  # init exploration parameter
update_turn = 2000000


def update(state, a, e):
    while 1 <= state.dealer <= 10 and 1 <= state.player <= 21:  # 合法状态
        d = state.dealer - 1
        p = state.player - 1
        explore = random.random()  # epsilon-greedy
        if explore >= e:  # 根据当前策略行进
            action = 0 if QTable[d][p][0] > QTable[d][p][1] else 1
        else:  # 随机游走
            action = random.randint(0, 1)
        next_state, reward = step(state, action)
        if 1 <= next_state.dealer <= 10 and 1 <= next_state.player <= 21:
            nextQ = max(QTable[next_state.dealer - 1][next_state.player-1])
        else:
            nextQ = 0
        QTable[d][p][action] += a * (reward + nextQ - QTable[d][p][action])


def test():
    s = State()
    s.initialize()
    while 1 <= s.dealer <= 10 and 1 <= s.player <= 21:
        d = s.dealer - 1
        p = s.player - 1
        action = 0 if QTable[d][p][1] < QTable[d][p][0] else 1
        next_state, reward = step(s, action)
        if reward == 1:
            return 1
        elif reward == -1:
            return -1
    return 0


print("Training in Q-learning...")
reward_data = []
for i in range(update_turn):
    s = State()
    s.initialize()
    update(s, alpha, epsilon)
    if (i+1) % 10000 == 0:
        r = 0
        for _ in range(10000):
            r += test()
        print(r)
        reward_data.append(r/10000.0)
    epsilon = epsilon * 0.9999 if epsilon > 0.1 else 0.1  # 每轮降低随机游走的概率
    alpha = alpha * 0.99 if alpha > 0.01 else 0.01
print("Success!")


if __name__ == '__main__':
    print(QTable)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.array([list(range(1, 11)) for _ in range(11, 22)])
    y = np.array([[i] * 10 for i in range(11, 22)])
    z = np.array([[max(QTable[i][j]) for i in range(10)] for j in range(10, 21)])
    ax.plot_wireframe(x, y, z, rstride=1, cstride=1)
    plt.title(f'alpha = {alpha}')
    plt.xticks(list(range(1, 11)))
    ax.set_xlabel('Dealer showing')
    plt.yticks(list(range(11, 22)))
    ax.set_ylabel('Player sum')
    plt.show()

    plt.subplot(111)
    plt.plot(reward_data)
    plt.show()
