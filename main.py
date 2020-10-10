# This is Easy21 project

from state import *
import QLearning as Q


def game():
    s = State()
    d = s.dealer - 1
    while 1 <= s.dealer <= 10 and 1 <= s.player <= 21:
        st = 21 * d + s.player - 1
        action = 0 if Q.QTable[st][1] < Q.QTable[st][0] else 1
        next_state, reward = step(s, action)
        if reward == 1:
            return 1
    return 0


def game2():
    s = State()
    while 1 <= s.dealer <= 10 and 1 <= s.player <= 21:
        action = random.randint(0, 1)
        next_state, reward = step(s, action)
        if reward == 1:
            return 1
    return 0


if __name__ == '__main__':
    res = 0
    for i in range(1000):
        res += game()
    print(res)
    res = 0
    for i in range(1000):
        res += game2()
    print(res)
    '''
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

