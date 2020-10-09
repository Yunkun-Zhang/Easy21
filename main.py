# This is Easy21 project

from state import *

if __name__ == '__main__':
    print('Game started!')
    s = State()
    print(f'The dealer\'s card is {s.dealer}.')
    while True:
        print(f'Your point is {s.player} now.', end=' ')
        x = input('Stick or hit? ')
        action = True if x == 'stick' else False
        next_state, reward = step(s, action)
        if reward == 1:
            if s.dealer < 1 or s.dealer > 21:
                print('The dealer busts!')
            else:
                print(f'Your point is {s.player}, and the dealer\'s is {s.dealer}.')
            print('Game over. YOU WIN!')
            exit()
        elif reward == -1:
            if s.player < 1 or s.player > 21:
                print('You bust!')
            else:
                print(f'Your point is {s.player}, and the dealer\'s is {s.dealer}.')
            print('Game over. You lose!')
            exit()
