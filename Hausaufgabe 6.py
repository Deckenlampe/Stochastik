import numpy as np
P = np.array([[1/3, 1/3, 1/3], [1/2, 1/4, 1/4], [1/2, 1/4, 1/4]])
P_grenz = np.array([[2/5, 2/5, 1/5], [2/5, 2/5, 1/5], [2/5, 2/5, 1/5]])

Q = np.array([[0.98, 0.02, 0],[0, 0.98, 0.02], [0.02, 0, 0.98]])
Q_grenz = np.array([[1/3, 1/3, 1/3], [1/3, 1/3, 1/3], [1/3, 1/3, 1/3]])

def matrix_diff(matrix, grenzmatrix):
    count = 0
    matrix_copy = matrix.copy()
    print(matrix_copy)
    print(grenzmatrix)
    while True:
        matrix = matrix @ matrix_copy  # Matrix multiplication
        count += 1
        # Compute the absolute difference between current and previous matrices
        diff = np.abs(grenzmatrix - matrix)
        # Check if any element has changed by less than or equal to 0.001
        if np.all(diff <= 0.001):
            print("Number of multiplications:", count)
            print(diff)
            break
        if count >= 500:
            print("Could not find the number of multiplications (<500)")
            print(matrix)
            break

matrix_diff(P, P_grenz)
matrix_diff(Q, Q_grenz)
