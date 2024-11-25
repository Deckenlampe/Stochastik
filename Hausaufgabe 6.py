import numpy as np
P = np.array([[1/3, 1/3, 1/3], [1/2, 1/4, 1/4], [1/2, 1/4, 1/4]])

Q = np.array([[0.98, 0.02, 0],[0, 0.98, 0.02], [0.02, 0, 0.98]])

def matrix_diff(matrix):
    count = 0

    while True:
        matrix_copy = matrix.copy()
        matrix = matrix @ matrix  # Matrix multiplication
        count += 1
        # Compute the absolute difference between current and previous matrices
        diff = np.abs(matrix - matrix_copy)
        # Check if any element has changed by less than or equal to 0.001
        if np.all(diff <= 0.001):
            print("Number of multiplications:", count)
            print(diff)
            break

matrix_diff(P)
matrix_diff(Q)
