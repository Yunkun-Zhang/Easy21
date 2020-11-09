# Easy21

EI339 小组编程作业 1，by 李俊龙，曲哲含，张昀焜



### state.py

搭建游戏环境：定义`State`类，定义`step`函数。

### QLearning.py

运行，学习完成后输出 Q table。

文件开头可调整学习参数：

```
alpha = 0.5            # 初始化学习率
epsilon = 1            # 初始化随机游走概率
min_alpha = 0.004      # 最小学习率
min_epsilon = 0.1      # 最小随机游走概率
update_turn = 1000000  # 更新轮数
```

### PolicyIteration.py

运行，学习完成后输出策略表。

文件开头可调整学习参数：

```
epoch_policy_eval = 100                 # 策略评估迭代轮数
epoch_policy_update = 20                # 策略优化迭代轮数
epoch_value_iteration_for_stick = 2000  # 计算玩家停牌后的状态的迭代轮数
```

### main.py

运行，等待两种方法学习完成后，输入模拟游戏对局数，可以测试不同学习方法的胜利、平局、失败概率。

取消文件末尾的注释，可以自己与庄家进行游戏！