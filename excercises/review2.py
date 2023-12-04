def sum(matrix, r, c):
    sum = 0
    for i in range(r+2):
        for j in range(c+2):
            sum += matrix[i][j]

    print(sum)
matrix = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]]

sum(matrix, 0, 0)
