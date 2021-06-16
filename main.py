import numpy as np
from Gram import Gram
import sys

epsilon = 1e-8


def list_to_matrix(vec_list):
    rows = len(vec_list)
    cols = len(vec_list[0])
    return np.array(vec_list, dtype=float)


def check_if_orthogonal(gs, mat):
    mat = np.transpose(mat)
    rows = len(mat)
    cols = len(mat[0])

    for row in range(rows):
        for col in range(1, cols - 1):
            dot_res = gs.dot(mat[row], mat[(row + col) % rows])
            if abs(dot_res) > epsilon:
                print("vec: ", row, " and vec: ", (row + col) % rows, "are not orth")
                print("dot result: ", dot_res)
                print(mat[row])
                print(mat[(row + col) % rows])

                return False

    for row in range(rows):
        norm = gs.norm(mat[row])
        if abs(norm - 1) > epsilon:
            print("vec: ", row, "is not normalized")
            print("norm: ", norm)
            return False

    return True


def test_gram_calculator():
    gs = Gram(np.eye(5, 5))
    for i in range(100):
        mat = np.random.rand(5, 5)
        res = gs.make_set_orthogonal_to_vec(mat).transpose()
        if not check_if_orthogonal(gs, res):
            print("Test failed")
            return

    print("Test passed")


def mission_3a():
    test = [[1, 2, 2, 0], [0, -1, -1, 0], [0, 0, 0, 3], [2, 1, 1, 3]]
    gs = Gram(np.eye(4, 4))
    res = gs.make_set_orthogonal_to_vec(list_to_matrix(test)).transpose()
    print("Orthogonal basis with standard inner product:")
    print(res)
    assert (check_if_orthogonal(gs, res))


def mission_3b():
    test = [[17, 7, 5], [7, 5, 1], [5, 1, 3]]
    gs = Gram(np.eye(3, 3))
    res = gs.make_set_orthogonal_to_vec(list_to_matrix(test)).transpose()
    print("Orthogonal basis for R2[x]")
    print(res)


def calculate_gs_for_gui(user_input):
    matrix = list_to_matrix(user_input)
    n = len(user_input)
    m = len(user_input[0])
    gs = Gram(np.eye(n, m))
    return gs.make_set_orthogonal_to_vec(matrix)


def main():
    test_gram_calculator()
    mission_3a()
    mission_3b()


main()
