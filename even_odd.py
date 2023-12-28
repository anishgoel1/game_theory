import random
import numpy as np


def even_odd_sim(trials):
    """
    :param trials: simulation duration
    :return: player 1 balance
    """
    p1_balance = 0
    game_mat = np.array([[-2, 3], [3, -4]])

    for _ in range(trials):
        p2_action = random.randint(0, 1)
        if random.uniform(0, 1) < 7 / 12:
            p1_balance += game_mat[0][p2_action]
        else:
            p1_balance += game_mat[1][p2_action]

    return p1_balance


episodes = 2000000
print("PLAYER ONE BALANCE: $", even_odd_sim(episodes))
print("EXPECTED BALANCE: $", round(1/12 * episodes))
