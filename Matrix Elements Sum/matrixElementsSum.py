def matrixElementsSum(matrix):
    summ = 0
    for i in range(len(matrix[0])):
        # print(i)
        for j in range(len(matrix)):
            if  matrix[j][i] == 0:
                break
                # matrix[i+1][j] = 0
            summ+=matrix[j][i]
            
    print(matrix)
    return summ
  
