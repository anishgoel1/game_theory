from saddle_point import saddle_point
import numpy as np


def optimal_strategy(mat):
    saddle = saddle_point(mat)
    if saddle is not None:
        p, q = 1, 1
        if saddle[0][0][0] == 2:
            p = 0
        if saddle[0][0][1] == 2:
            q = 0
        return p, q, saddle[0][1]  # p, q, v
    else:
        p = (mat[1][1] - mat[1][0]) / ((mat[0][0] - mat[0][1]) + (mat[1][1] - mat[1][0]))
        q = (mat[1][1] - mat[0][1]) / (mat[0][0] - mat[0][1] + mat[1][1] - mat[1][0])
        v = (mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]) / (mat[0][0] - mat[0][1] + mat[1][1] - mat[1][0])
        return p, q, v


example_1 = np.array([[-2, 3], [3, -4]])
result_1 = optimal_strategy(example_1)
print("EXAMPLE 1: "
      "p:", "{:.3f}".format(result_1[0]),
      ", q:", "{:.3f}".format(result_1[1]),
      ", v:", "{:.3f}".format(result_1[2]))

example_2 = np.array([[0, -10], [1, 2]])
result_2 = optimal_strategy(example_2)
print("EXAMPLE 2: "
      "p:", "{:.3f}".format(result_2[0]),
      ", q:", "{:.3f}".format(result_2[1]),
      ", v:", "{:.3f}".format(result_2[2]))
