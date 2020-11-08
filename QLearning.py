# Training in Q-learning

from state import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import time

QTable = np.zeros((10, 21, 2))  # 21*10状态、2种行动
alpha = 0.5  # 初始化学习率
epsilon = 1  # 初始化随机游走概率
update_turn = 1000000  # 更新轮数


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
            nextQ = reward
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
start = time.clock()
reward_data = []
freq = 10000
for i in range(update_turn):
    s = State()
    s.initialize()
    update(s, alpha, epsilon)
    """ test
    if (i+1) % freq == 0:
        r = 0
        for _ in range(10000):
            r += test()
        reward_data.append(r/10000.0)
    """
    epsilon = epsilon * 0.999 if epsilon > 0.1 else 0.1  # 每轮降低随机游走的概率 (0.1)
    alpha = alpha * 0.99 if alpha > 0.004 else 0.004  # (0.0039)
print("Success!")
print(f'Time used: {time.clock() - start}s')


def plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.array([list(range(1, 11)) for _ in range(11, 22)])
    y = np.array([[i] * 10 for i in range(11, 22)])
    z = np.array([[max(QTable[i][j]) for i in range(10)] for j in range(10, 21)])
    ax.plot_wireframe(x, y, z, rstride=1, cstride=1)
    plt.title(f'Value-state')
    plt.xticks(list(range(1, 11)))
    ax.set_xlabel('Dealer showing')
    plt.yticks(list(range(11, 22)))
    ax.set_ylabel('Player sum')
    ax.set_zlabel('Value of state')
    # plt.show()
    plt.savefig(f'sv_a_{alpha}_e_{epsilon}_t_{update_turn}.png')
    plt.close()

    plt.subplot(111)
    x = [i * freq for i in range(update_turn // freq)]
    plt.xlabel('update turn')
    plt.ylabel('avg reward')
    plt.plot(x, reward_data)
    # plt.show()
    plt.savefig(f're_a_{alpha}_e_{epsilon}_t_{update_turn}.png')


if __name__ == '__main__':
    with open(f'storage/re_a_{alpha}_e_{epsilon}_t_{update_turn}.txt', 'w') as f:
        for i in reward_data:
            f.write(f'{i} ')
    print(QTable)
    # plot()
