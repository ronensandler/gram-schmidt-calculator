import numpy as np
from Gram import Gram
import sys


def list_to_matrix(vec_list):
    rows = len(vec_list)
    cols = len(vec_list[0])
    return np.array(vec_list, dtype=float)


def check_if_ortogonal(mat):
    mat = np.transpose(mat)
    rows = len(mat)
    cols = len(mat[0])

    for row in range(rows):
        for col in range(1, cols):
            dot_res = np.dot(mat[row], mat[(row + col) % rows])
            if abs(dot_res) > sys.float_info.epsilon:
                print("vec: ", row, " and vec: ", (row + col) % rows, "are not orth")
                print("dot result: ", dot_res)
                return False

    for row in range(rows):
        norm = np.linalg.norm(mat[row])
        if abs(norm - 1) > sys.float_info.epsilon:
            print("vec: ", row, "is not normalized")
            print("norm: ", norm)
            return False

    return True


def main():
    mat = np.random.rand(3, 3)
    print(mat)
    test = [[1, 2, 2, 0], [0, -1, -1, 0], [0, 0, 0, 3], [2, 1, 1, 3]]
    gs = Gram(np.eye(3, 3))
    gs2 = Gram(np.eye(4, 4))
    base = gs2.make_set_orthogonal_to_vec(list_to_matrix(test).transpose())
    res = gs.make_set_orthogonal_to_vec(mat).transpose()

    print(" v1 dot v2:", np.dot(res[0], res[1]))
    print(" v2 dot v3:", np.dot(res[1], res[2]))
    print(" v1 dot v3:", np.dot(res[0], res[2]))
    print(" v1 norm:", np.linalg.norm(res[0]))
    print(" v2 norm:", np.linalg.norm(res[1]))
    print(" v3 norm:", np.linalg.norm(res[2]))


main()
