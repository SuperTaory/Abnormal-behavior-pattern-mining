import numpy as np
from math import sqrt, pow
from numpy.matlib import repmat
import matplotlib.pyplot as plt


def dtw_distance(r, t):
    M = len(r)
    N = len(t)
    r_array = np.matrix(r)
    t_array = np.matrix(t)
    # 初始化原始距离矩阵
    distance_classical = abs(repmat(r_array.T, 1, N) - repmat(t_array, M, 1))
    # distance_classical = np.zeros((M, N))
    # for i in range(0,M):
    #     for j in range(0,N):
    #         distance_classical[i,j] = round(sqrt(pow((i-j), 2) + pow((r[i] - t[j]), 2)), 1)
    print('原始距离矩阵dist:\n', distance_classical)

    # 初始化累积距离矩阵
    D = np.zeros(np.shape(distance_classical))
    D[0, 0] = distance_classical[0, 0]
    for m in range(1, M):
        D[m, 0] = distance_classical[m, 0] + D[m - 1, 0]
    for n in range(1, N):
        D[0, n] = distance_classical[0, n] + D[0, n - 1]
    for m in range(1, M):
        for n in range(1, N):
            D[m, n] = distance_classical[m, n] + min(D[m - 1, n], min(D[m - 1, n - 1], D[m, n - 1]))
    # dist = D[-1, -1]
    print('累积距离矩阵d:\n', D)
    return D


def show_path(s1, s2):
    D = dtw_distance(s1, s2)
    M = len(s1)
    N = len(s2)
    # 计算最短累计距离路径
    mat = np.ones((M, N))
    mat = np.array(mat)
    # mat[1, 2] = 0
    # print(mat)
    i = M - 1
    j = N - 1
    mat[i, j] = 0
    while True:
        if i == 0 and j ==0:
            break
        elif i == 0 and j != 0:
            j -= 1
            mat[i, j] = 0
        elif j == 0 and i != 0:
            i -= 1
            mat[i, j] = 0
        else:
            minum = min(D[i - 1, j], min(D[i - 1, j - 1], D[i, j - 1]))
            if D[i - 1, j - 1] == minum:
                i -= 1
                j -= 1
                mat[i, j] = 0
            elif D[i - 1, j] == minum:
                i -= 1
                mat[i, j] = 0
            else:
                j -= 1
                mat[i, j] = 0

    plt.subplot(2, 2, 2)
    plt.pcolor(mat, edgecolors='k', linewidths=0.5)
    plt.title('Dynamic Time Warping (%f)' % D[-1, -1])

    plt.subplot(2, 2, 4)
    plt.plot(s2, range(N), 'g')

    plt.subplot(2, 2, 1)
    plt.plot(range(M), s1, 'r')

    plt.show()
    # print('DTW距离:', dist)

# # s1 = [8, 7, 6, 7, 6, 6, 7, 8, 8, 7, 6]
# # s1 = [8, 7, 6, 6, 6, 7, 8, 8, 8, 7, 6]
# s1 = [3.1, 4.15, 5.12, 5.1, 5.2, 4.12]
s1 = [1, 2, 3, 4, 5, 5, 5, 4]
# # s1 = [3, 4, 5, 5, 5, 4]
s2 = [3, 4, 5, 5, 5, 4]
# # display(s1, s2)
#dtw_distance(s1, s2)
show_path(s1, s2)
