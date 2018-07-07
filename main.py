import random

def main():
    """
    ゲームを実行する
    """
    print('Rolling the dice...')

    (d1, d2) = (roll_dice(), roll_dice())
    print('Die 1: {}'.format(d1))
    print('Die 2: {}'.format(d2))

    print('Total value: {}'.format(d1 + d2))

def roll_dice():
    """
    サイコロを振り、出た目を返します
    """
    return random.randint(1, 6)


if __name__ == '__main__':
    main()
