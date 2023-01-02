T = [[4, 1, 1, 3],
     [2, 0, 2, 1],
     [3, 1, 5, 1]]
Tp = [[4, 5, 6, 9],
      [6, 6, 8, 10],
      [9, 10, 15, 16]]


def somme_max(T, i, j):
    if i == 0 and j == 0:
        return T[i][j]
    if i > 0:
        return
