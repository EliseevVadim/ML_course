import numpy as np
import math


def foster_stuart_criterion(x):
    n = len(x)
    p = np.ones(n - 1)
    q = np.ones(n - 1)

    for i in range(1, n):
        for j in range(i):
            if x[i] >= x[j]:
                p[i - 1] = 0
            if x[i] <= x[j]:
                q[i - 1] = 0
            if q[i - 1] + p[i - 1] == 0:
                break
    t = abs(np.sum(p - q) / np.sqrt(2 * np.sum(1 / np.arange(2, n))))
    return t


def means_comparison_criterion(x):
    n = len(x)
    n1 = math.floor(n / 2)
    n2 = n - n1 - 1
    mean_1 = np.mean(x[:n1])
    mean_2 = np.mean(x[n1:])
    var_1 = np.var(x[:n1])
    var_2 = np.var(x[n1:])
    t = np.abs(mean_1 - mean_2) / (np.sqrt(var_1 / n1) + np.sqrt(var_2 / n2))
    return t


def se_test(x):
    x_sorted = np.sort(x)
    m = np.median(x_sorted)

    below_median = x_sorted[x_sorted < m]
    above_median = x_sorted[x_sorted > m]

    def get_series(arr):
        arr_diff = np.diff(np.where(np.diff(arr) != 0))
        series_starts = np.where(arr_diff != 1)[0] + 1
        return np.split(arr, series_starts)

    x1 = get_series(below_median)
    x2 = get_series(above_median)

    n1 = len(x1)
    n2 = len(x2)
    sc = n1 + n2

    s_max = max([len(seq) for seq in x1 + x2])

    return not (s_max < np.floor(3.3 * (np.log(len(x)) + 1)) and sc > np.floor(
        0.5 * (len(x) + 1 - 1.96 * np.sqrt(len(x) - 1))))
