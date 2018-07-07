import random

def main():
    """
    ゲームを実行する
    """
    print('Rolling the dice...')

    (d1, d2) = (roll_dice(), roll_dice())
    print('Die 1: {}'.format(d1))
    print('Die 2: {}'.format(d2))

    total = d1 + d2
    print('Total value: {}'.format(total))

    # 勝敗を出力
    result = 'won' if total > 7 else 'lost'
    print('You {}'.format(result))


def roll_dice():
    """
    サイコロを振り、出た目を返します
    """
    return random.randint(1, 6)


if __name__ == '__main__':
    main()
