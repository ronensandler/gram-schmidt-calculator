import numpy as np
import sys


def is_pos_def(matrix):
    return np.all(np.linalg.eigvals(matrix) > 0)


def is_zero(vec):
    '''returns true if vec is a zero vector'''
    return not np.any(np.absolute(vec) > sys.float_info.epsilon)


class Gram:
    def __init__(self, mult):
        if not is_pos_def(mult):
            raise Exception("Invalid inner product")
        self.mult = mult

    @staticmethod
    def static_norm(mult, v):
        return np.sqrt(Gram.static_dot(mult, v, v))

    @staticmethod
    def static_dot(mult, v1, v2):
        return np.dot(v1.transpose(), np.dot(mult, v2))

    def dot(self, v1, v2):
        return Gram.static_dot(self.mult, v1, v2)

    def norm(self, v):
        return Gram.static_norm(self.mult, v)

    def make_set_orthogonal_to_vec(self, vectors):
        result = []
        m = len(vectors)
        while len(vectors) != 0:
            if len(vectors[0]) == 0:
                break

            vec = vectors[:, 0]
            vectors = np.delete(vectors, 0, axis=1)
            if is_zero(vec):
                continue

            # Normalize
            normalized = np.divide(vec, self.norm(vec))

            result.append(normalized)
            if len(result) == m:
                break

            # Make all other vectors independent to the vector
            temp = []
            for orig in vectors.transpose():
                temp.append(orig - (self.dot(normalized, orig) * normalized))

            vectors = np.array(temp).transpose()

        return np.array(result)
