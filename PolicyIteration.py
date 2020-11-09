# Training in Policy Iteration

import numpy as np
import copy
import time

# 参数
epoch_policy_eval = 100  # 策略评估迭代轮数
epoch_policy_update = 20  # 策略优化迭代轮数
epoch_value_iteration_for_stick = 2000  # 计算玩家停牌后的状态的迭代轮数

# 初始化
posi_poss = 2 / 30.0  # 正数牌的概率
neg_poss = 1 / 30.0  # 负数牌的概率
PolicyTable = np.random.randint(0, 2, (21, 10))  # 随机初始化策略矩阵
ValueTable = np.zeros((21, 10))
ValueTable_after_stick = np.zeros((21, 21))

print("Initializing policy iteration...")
start = time.clock()

# 对玩家停止拿牌后的状态使用策略迭代方法（庄家视角）确定期望收益
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


# 学习
print("Training in policy iteration...")
for i in range(epoch_policy_update):
    for j in range(epoch_policy_eval):
        policy_eval_update()
    policy_improvement_update()
print("Success!")
print(f"Time used: {time.clock() - start:.4f}s")


if __name__ == "__main__":
    print(PolicyTable)
