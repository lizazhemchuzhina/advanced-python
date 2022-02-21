import numpy as np

from hw_03.matrix.easy import EasyMatrix
from hw_03.matrix.medium import MediumMatrix
from hw_03.matrix.hard import HardMatrix


def gen_easy():
    np.random.seed(0)
    a_mat = EasyMatrix(np.random.randint(0, 10, (10, 10)))
    b_mat = EasyMatrix(np.random.randint(0, 10, (10, 10)))
    with open('artifacts/easy/matrix+.txt', 'w') as file:
        file.write((a_mat + b_mat).__str__())
    with open('artifacts/easy/matrix*.txt', 'w') as file:
        file.write((a_mat * b_mat).__str__())
    with open('artifacts/easy/matrix@.txt', 'w') as file:
        file.write((a_mat @ b_mat).__str__())


def gen_medium():
    np.random.seed(0)
    a_mat = MediumMatrix(np.random.randint(0, 10, (10, 10)))
    b_mat = MediumMatrix(np.random.randint(0, 10, (10, 10)))
    with open('artifacts/medium/matrix+.txt', 'w') as file:
        file.write((a_mat + b_mat).__str__())
    with open('artifacts/medium/matrix*.txt', 'w') as file:
        file.write((a_mat * b_mat).__str__())
    with open('artifacts/medium/matrix@.txt', 'w') as file:
        file.write((a_mat @ b_mat).__str__())


def gen_hard():
    a_mat = HardMatrix([[30, 30], [0, 0]])
    b_mat = HardMatrix([[100, 100], [100, 100]])
    c_mat = HardMatrix([[10, 20], [20, 10]])
    d_mat = HardMatrix([[100, 100], [100, 100]])
    with open('artifacts/hard/A.txt', 'w') as file:
        file.write((a_mat).__str__())
    with open('artifacts/hard/B.txt', 'w') as file:
        file.write((b_mat).__str__())
    with open('artifacts/hard/C.txt', 'w') as file:
        file.write((c_mat).__str__())
    with open('artifacts/hard/D.txt', 'w') as file:
        file.write((d_mat).__str__())
    ab_mat = a_mat @ b_mat
    c_mat._matmul_hashes = {}
    cd_mat = c_mat @ d_mat
    with open('artifacts/hard/AB.txt', 'w') as file:
        file.write((ab_mat).__str__())
    with open('artifacts/hard/CD.txt', 'w') as file:
        file.write((cd_mat).__str__())
    with open('artifacts/hard/hash.txt', 'w') as file:
        file.write("AB hash:\n" + (ab_mat.__hash__()).__str__() +
                   '\nCD hash:\n' + (cd_mat.__hash__()).__str__())


if __name__ == '__main__':
    gen_easy()
    gen_medium()
    gen_hard()
