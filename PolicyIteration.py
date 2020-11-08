# Training in Policy Iteration

import numpy as np
import copy
from state import *
import matplotlib.pyplot as plt
import time

print("Initializing policy iteration...")
start = time.clock()

posi_poss = 2 / float(30)
neg_poss = 1 / float(30)

epoch_policy_eval = 100  # 策略评估迭代轮数
epoch_policy_update = 20  # 策略优化迭代轮数
epoch_value_iteration_for_stick = 2000  # 计算玩家停牌后的状态的迭代轮数

PolicyTable = np.random.randint(0, 2, (21, 10))  # 随机初始化策略矩阵

ValueTable = np.zeros((21, 10))

# 对玩家停止拿牌后的状态使用策略迭代方法（庄家视角）确定期望收益
ValueTable_after_stick = np.zeros((21, 21))
for i in range(21):
    for j in range(15, 21):
        ValueTable_after_stick[i][j] = 1 if i > j else 0 if i == j else -1

for epoch in range(epoch_value_iteration_for_stick):
    tmpvaluetable = copy.deepcopy(ValueTable_after_stick)
    for i in range(21):
        for j in range(15):
            tmpvalue = 0
            for t in range(-10, 11):
                if t == 0:
                    continue
                poss = neg_poss if t < 0 else posi_poss
                if j + t < 0 or j + t > 20:
                    tmpvalue += poss * 1
                else:
                    tmpvalue += poss * tmpvaluetable[i][j + t]
            ValueTable_after_stick[i][j] = tmpvalue


def policy_eval_update():
    tmpvaluetable = copy.deepcopy(ValueTable)
    for i in range(0, 21):
        for j in range(0, 10):
            tmpvalue = 0
            if PolicyTable[i][j] == 0:  # 拿牌
                for t in range(-10, 11):
                    if t == 0: continue
                    if t > 0:
                        poss = posi_poss
                    else:
                        poss = neg_poss
                    if i + t < 0 or i + t > 20:
                        tmpvalue += poss * -1
                    else:
                        tmpvalue += tmpvaluetable[i + t][j] * poss
            else:  # 停止拿牌
                tmpvalue = ValueTable_after_stick[i][j]
            ValueTable[i][j] = tmpvalue


def policy_improvement_update():
    for i in range(21):
        for j in range(10):
            tmpvalue_1 = ValueTable_after_stick[i][j]
            tmpvalue_0 = 0
            for t in range(-10, 11):
                if t == 0: continue
                if t > 0:
                    poss = posi_poss
                else:
                    poss = neg_poss
                if i + t < 0 or i + t > 20:
                    tmpvalue_0 += poss * -1
                else:
                    tmpvalue_0 += poss * ValueTable[i + t][j]
            PolicyTable[i][j] = 0 if tmpvalue_0 > tmpvalue_1 else 1


def test():
    s = State()
    s.initialize()
    while 1 <= s.dealer <= 10 and 1 <= s.player <= 21:
        action = PolicyTable[s.player - 1][s.dealer - 1]
        next_state, reward = step(s, action)
        if reward == 1:
            return 1
        elif reward == -1:
            return -1
    return 0


print("Training in policy iteration...")
reward_data = []
r = 0
for _ in range(10000):
    r += test()
reward_data.append(r/10000.0)
for i in range(epoch_policy_update):
    for j in range(epoch_policy_eval):
        policy_eval_update()
    policy_improvement_update()
    """ test
    r = 0
    for _ in range(10000):
        r += test()
    reward_data.append(r/10000.0)
    """
print("Success!")
print(f"Time used: {time.clock() - start}s")


if __name__ == "__main__":
    plt.xlabel('iter number')
    plt.ylabel('avg reward')
    plt.plot(reward_data)
    # plt.show()
    plt.savefig(f'storage/re_epe_{epoch_policy_eval}_epu_{epoch_policy_update}.png')
