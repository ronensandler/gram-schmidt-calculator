import numpy as np
import sys


class Gram:
    def __init__(self, mult):
        #if not self.is_pos_def(mult):
        #    raise Exception("Invalid inner product")
        self.mult = mult

    def dot(self, v1, v2):
        return np.dot(v1.transpose(), np.dot(self.mult, v2))

    def make_set_orthogonal_to_vec(self, vectors):
        result = []

        while len(vectors) != 0:
            vec = vectors[:, 0]
            vectors = np.delete(vectors, 0, axis=1)
            if self.is_zero(vec):
                continue

            # Normalize
            normalized = np.divide(vec, np.linalg.norm(vec))

            result.append(normalized)

            # Make all other vectors independent to the vector
            temp = []
            for orig in vectors.transpose():
                temp.append(orig - (self.dot(normalized, orig) * normalized))

            vectors = np.array(temp).transpose()

        return np.array(result)

    def is_zero(self, vec):
        '''returns true if vec is a zero vector'''
        return not np.any(np.absolute(vec) > sys.float_info.epsilon)

    def is_pos_def(self, A):
        if np.allclose(A, A.H):
            return np.all(np.linalg.eigvals(A) > 0)
        return False
