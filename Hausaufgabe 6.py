import numpy as np
P = np.array([[1/3, 1/3, 1/3], [1/2, 1/4, 1/4], [1/2, 1/4, 1/4]])
P_grenz = np.array([[2/5, 2/5, 1/5], [2/5, 2/5, 1/5], [2/5, 2/5, 1/5]])

Q = np.array([[0.98, 0.02, 0],[0, 0.98, 0.02], [0.02, 0, 0.98]])
Q_grenz = np.array([[1/3, 1/3, 1/3], [1/3, 1/3, 1/3], [1/3, 1/3, 1/3]])

def matrix_diff(matrix):
    count = 0
    matrix_copy = matrix.copy()
    limit = np.linalg.matrix_power(matrix, 10000)
    print(limit)
    while True:
        matrix = matrix @ matrix_copy  # Matrix multiplication
        count += 1
        # Compute the absolute difference between current and previous matrices
        diff = np.abs(limit - matrix)
        # Check if any element has changed by less than or equal to 0.001
        if np.all(diff <= 0.001):
            print("To the power of", count+1)
            print(diff)
            break
        if count >= 500:
            print("Could not find the number of multiplications (<500)")
            print(matrix)
            break

matrix_diff(P)
matrix_diff(Q)
