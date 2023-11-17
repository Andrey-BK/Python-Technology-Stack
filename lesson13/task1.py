import random

def create_random_matrix(rows, cols):
    matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    return matrix

def add_matrices(matrix1, matrix2):
    result_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return result_matrix

# функция принимает на вход размер матрицы, затем гененирует две матрицы указанного размера, 
# заполняет их случайными числами от 1 до 100 и возвращает результат их сложения
def my_function(rows, cols):
    return add_matrices(create_random_matrix(rows, cols), create_random_matrix(rows, cols))