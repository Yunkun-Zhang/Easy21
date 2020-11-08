# This is Easy21 project

from state import *
import QLearning as Q
import PolicyIteration as PI


def game(strategy):
    s = State()
    s.initialize()
    while 1 <= s.dealer <= 10 and 1 <= s.player <= 21:
        if strategy == "ql":
            d = s.dealer - 1
            p = s.player - 1
            action = 0 if Q.QTable[d][p][1] < Q.QTable[d][p][0] else 1
        elif strategy == "rand":
            action = random.randint(0, 1)
        elif strategy == "pi":
            action = PI.PolicyTable[s.player - 1][s.dealer - 1]
        next_state, reward = step(s, action)
        if reward == 1:
            return 1
        elif reward == -1:
            return -1
    return 0


if __name__ == '__main__':
    Stategy_dict = {"RANDOM": 'rand', "Q-Learning": 'ql', "Policy Iteration": "pi"}
    round = int(input("\nEnter the rounds you want to play: "))
    print("")

    for key in Stategy_dict:
        print("Playing with strategy:", key)
        win = 0
        draw = 0
        lose = 0
        for i in range(round):
            res = game(Stategy_dict[key])
            if res == 1:
                win += 1
            elif res == 0:
                draw += 1
            else:
                lose += 1
        print("------ Statistics for strategy:", key, "------")
        print(f"WIN:\t{win}  \t{float(win * 100) / round}%")
        print(f"DRAW:\t{draw}  \t{float(draw * 100) / round}%")
        print(f"LOSE:\t{lose}  \t{float(lose * 100) / round}%")
        print("")

    '''
    # play the game yourself!
    print('Game started!')
    s = State()
    print(f'The dealer\'s card is {s.dealer}.')
    while True:
        print(f'Your point is {s.player} now.')
        st = 21 * (s.dealer - 1) + s.player - 1
        # x = input('Stick or hit? ')
        # action = True if x == 'stick' else False
        action = Q.QTable[st][1] > Q.QTable[st][0]
        next_state, reward = step(s, action)
        if reward == 1:
            if s.dealer < 1 or s.dealer > 21:
                print('The dealer busts!')
            else:
                print(f'Your point is {s.player}, and the dealer\'s is {s.dealer}.')
            print('Game over. YOU WIN!')
            break
        elif reward == -1:
            if s.player < 1 or s.player > 21:
                print('You bust!')
            else:
                print(f'Your point is {s.player}, and the dealer\'s is {s.dealer}.')
            print('Game over. You lose!')
            break
    '''

