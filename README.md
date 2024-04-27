import numpy as np

def generate_matrix(N):
    # Генерация матрицы А с заполнением случайными числами в интервале [-10, 10]
    A = np.random.randint(-10, 11, size=(N, N))
    return A

def is_prime(num):
    # Функция для проверки, является ли число простым
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(matrix):
    # Функция для подсчета простых чисел в нечетных столбцах матрицы B
    B = matrix[::2, 1::2]
    count = sum(is_prime(num) for num in np.nditer(B))
    return count

def generate_F(A, B, C):
    # Формирование матрицы F на основе условий
    F = A.copy()
    perimeter_product = np.prod(np.concatenate([C[0], C[-1], C[1:-1, 0], C[1:-1, -1]]))
    if count_primes(B) > perimeter_product:
        F[:, [0, -1]] = F[:, [-1, 0]]
    else:
        F[:, [1, -2]] = F[:, [-2, 1]]
    return F

def main():
    # Ввод размерности матрицы N
    N = int(input("Введите размерность матрицы N: "))
    K = int(input("Введите значение K: "))

    # Генерация матрицы А
    A = generate_matrix(N)
    print("Матрица A:")
    print(A)

    # Генерация матриц B, C, D, E
    B = np.random.randint(-10, 11, size=(N//2, N//2))
    C = np.random.randint(-10, 11, size=(N//2, N//2))
    D = np.random.randint(-10, 11, size=(N//2, N//2))
    E = np.random.randint(-10, 11, size=(N//2, N//2))
    print("Матрица B:")
    print(B)
    print("Матрица C:")
    print(C)
    print("Матрица D:")
    print(D)
    print("Матрица E:")
    print(E)

    # Формирование матрицы F
    F = generate_F(A, B, C)
    print("Матрица F:")
    print(F)

    # Вычисление определителя матрицы A
    det_A = np.linalg.det(A)
    # Вычисление суммы диагональных элементов матрицы F
    diagonal_sum_F = np.trace(F)

    if det_A > diagonal_sum_F:
        result = np.dot(A, A.T) - K * F
    else:
        G = np.tril(A)
        result = (np.linalg.inv(A) + np.linalg.inv(G) - F - K) * K

    print("Результат:")
    print(result)

if __name__ == "__main__":
    main()
