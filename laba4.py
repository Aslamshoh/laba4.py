# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное заполнение, а целенаправленное. Вид матрицы А: 

В  С  
D  Е  
30.  Формируется матрица F следующим образом: скопировать в нее А и  если в В количество простых чисел в нечетных столбцах, чем произведение чисел по периметру С, то поменять местами  С и В симметрично, иначе С и В поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * F, иначе вычисляется выражение (A-1 +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно 

import numpy as np
from matplotlib import pyplot as plt

# Получение входных данных
n = int(input("Введите размер матрицы N : "))
while n < 6:
    n = int(input("Введите размер матрицы: "))
k = int(input("Введите коэффициент K: "))

# Создание матрицы A
A = np.random.randint(-10, 11, size=(n, n))
F = A.copy()
print("Матрица A:\n", A, "\n")

# Вспомогательные функции для вывода матрицы
def print_mat(mat, description):
    plt.matshow(mat, cmap='inferno')
    plt.title(description)
    plt.colorbar()
    plt.show()

def print_mat1(mat, description):
    plt.figure(figsize=(10, 4))
    plt.plot(mat[0, :], 'o-', color='purple')
    plt.title(description)
    plt.xlabel('Индекс столбца')
    plt.ylabel('Значение элемента')
    plt.grid(True)
    plt.show()

def print_mat2(F, description):
    column_sums = np.sum(F, axis=0)
    plt.bar(range(len(column_sums)), column_sums)
    plt.title('Столбчатая диаграмма сумм значений столбцов матрицы F')
    plt.xlabel('Индекс столбца')
    plt.ylabel('Сумма значений')
    plt.show()

def print_mat3(F, description):
    column_sums = np.sum(np.abs(F), axis=0)
    labels = [f'Столбец {i + 1}' for i in range(F.shape[1])]
    plt.pie(column_sums, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(description)
    plt.show()

# Функция для проверки простоты числа
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Функция для подсчета количества простых чисел в нечетных столбцах матрицы
def count_primes_in_odd_columns(mat):
    count = 0
    for i in range(1, mat.shape[1], 2):
        for j in range(mat.shape[0]):
            if is_prime(mat[j, i]):
                count += 1
    return count

# Функция для подсчета произведения чисел по периметру матрицы
def product_of_perimeter(mat):
    product = 1
    for i in range(mat.shape[0]):
        product *= mat[i, 0]
        product *= mat[i, mat.shape[1] - 1]
    for j in range(1, mat.shape[1] - 1):
        product *= mat[0, j]
        product *= mat[mat.shape[0] - 1, j]
    return product

# Функция для формирования матрицы F
def form_matrix_F(A, B, C, D, E):
    size = len(A) // 2
    prime_count = count_primes_in_odd_columns(E)
    perimeter_product = product_of_perimeter(C)

    # Определение, какие подматрицы менять местами
    if prime_count > perimeter_product:
        B, C = np.fliplr(C), np.fliplr(B)
    else:
        C, E = E, C

    # Формирование матрицы F из подматриц
    F[:size, :size] = B
    F[:size, size:] = C
    F[size:, :size] = D
    F[size:, size:] = E
    return F

# Деление матрицы A на подматрицы B, C, D, E
size = n // 2
B, C, D, E = A[:size, :size], A[:size, size:], A[size:, :size], A[size:, size:]

print_mat(A, "Матрица A")
print_mat(B, "Матрица B")
print_mat(C, "Матрица C")
print_mat(D, "Матрица D")
print_mat(E, "Матрица E")

# Формирование матрицы F
F = form_matrix_F(A, B, C, D, E)
print("Матрица F после перестановки:\n", F, "\n")
print_mat(F, "Матрица F")
print_mat1(F, "Матрица F")
print_mat2(F, "Матрица F")
print_mat3(F, "Матрица F")

# Вычисление результата в зависимости от условия
if np.linalg.det(A) > np.trace(F):
    result = np.linalg.inv(A).dot(A.T) - k * np.linalg.inv(F)
else:
    G = np.tril(A)
    result = (A + G - F.T) * k

# Вывод итоговой матрицы
print("Результат:\n", result)
print_mat(result, "Результат")
