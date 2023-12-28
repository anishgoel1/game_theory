import numpy as np


def saddle_point(mat):
    """
    :param mat: game matrix // payoff matrix
    :return: saddle point [(row, col), value], 1-indexed
    """
    row_min, col_max, saddle = [], [], []
    for row in mat:
        row_min.append(min(row))
    for col in mat.transpose():
        col_max.append(max(col))

    for idx, val in enumerate(row_min):
        if val in col_max:
            saddle.append([(idx + 1, col_max.index(val) + 1), val])

    return saddle if len(saddle) > 0 else None


# Example 1:
A_1 = np.array([[4, 1, -3], [3, 2, 5], [0, 1, 6]])
print("SADDLE POINT A1:", saddle_point(A_1))

# Example 2:
A_2 = np.array([[3, 1, 1, 0], [0, 1, 2, 0], [1, 0, 2, 1], [3, 1, 2, 2]])
print("SADDLE POINT A2:", saddle_point(A_2))
