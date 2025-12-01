# BOJ 1158
from os import remove


def josephus_problem(n, k):

    arr = list(range(1, n + 1))
    result_arr = []
    cur_index = k - 1

    while arr:
        result_arr.append(arr.pop(cur_index))
        if len(arr) != 0:
            cur_index = (cur_index + (k - 1)) % len(arr)

    return print("<", ", ".join(map(str, result_arr)), ">", sep='')



n, k = map(int, input().split())
josephus_problem(n, k)
