import numpy as np


def main():
    """
    This is my solution implemented in Python. In this implementation, as soon as the first saddle
    point is found, the program returns the index of the point and terminates the search. This is
    because there can only be at most one saddle point (as defined in the question) for any given
    matrix.

    For the proof of the above statement, see README.md
    """
    # Given matrix
    matrix_1 = np.array(
        [[22.128, 71.599, 24.083, 79.442, 8.4186, 55.744],
         [14.83, 67.261, 85.3, 38.613, 59.892, 51.837],
         [6.6377, 93.302, 52.451, 62.743, 33.464, 34.494],
         [23.96, 91.573, 86.388, 28.882, 94.461, 53.222],
         [7.1165, 81.087, 44.558, 13.754, 85.023, 18.426]])

    # Test matrices
    matrix_2 = np.array([[1, 2], [0, 1]])         # A[0, 0] = 1
    matrix_3 = np.array([[1, 2], [1, 1]])         # A has no saddle points
    matrix_4 = np.array([[8, 14, 7], [5, 21, 6]]) # A[0, 2] = 7

    # Set matrix A to whichever input matrix defined above
    A = matrix_1

    print("\nMatrix A:")
    print(A)

    sp_index = get_saddle_point(A)

    if not sp_index:
        print("\nThe matrix A has no saddle points.")
    else:
        print("\nThe saddle points of the matrix A are:\nA" + \
            str(sp_index) + ": " + str(A[sp_index[0], sp_index[1]]))


def get_saddle_point(matrix) -> list:
    """
    This function iterates through an m x n matrix and checks if each entry is
    a saddle point as defined above. If an entry is a saddle point, it is
    added to a dictionary where the key value pair is the index of the entry and
    the value of the entry.

    Precondition: <matrix> is a numpy.array
    Postcondition: returns a dictionary containing all saddle points of
    <matrix>.
    """
    matrix_t = matrix.transpose()
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if exclusive_min(j, matrix[i]) and exclusive_max(i, matrix_t[j]):
                return [i, j]
    return None


def exclusive_min(index: int, lst: list) -> bool:
    """
    This function checks if lst[index] is strictly smaller than every other
    element in lst.

    Precondition: 0 <= index < len(lst) (i.e. <index> is valid for lst)
    Postcondition: returns True if lst[index] is strictly smaller than every
    other element in lst, False otherwise.
    """
	length = len(lst)
    for i in range(length):
        if i != index and lst[i] <= lst[index]:
            return False
    return True


def exclusive_max(index: int, lst: list) -> bool:
    """
    This function checks if lst[index] is strictly greater than every other
    element in lst.

    Precondition: 0 <= index < len(lst) (i.e. <index> is valid for lst)
    Postcondition: returns True if lst[index] is strictly greater than every
    other element in lst, False otherwise.
    """
	length = len(lst)
    for i in range(length):
        if i != index and lst[i] >= lst[index]:
            return False
    return True


if __name__ == "__main__":
    main()
