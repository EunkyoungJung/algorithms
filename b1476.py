"""
백준#1476
https://www.acmicpc.net/problem/1476
"""

"""
esm에 해당하는 연도 구하기
"""


def add_esm_year(esm):
    e, s, m = [x+1 for x in esm]

    if m > 19:
        m -= 19
    if s > 28:
        s -= 28
    if e > 15:
        e -= 15

    return [e, s, m]


def convert_esm_into_year(target_esm):
    esm = [1, 1, 1]
    year = 1
    while True:
        if esm == target_esm:
            return year
            break
        year += 1
        esm = add_esm_year(esm)


e, s, m = [int(x) for x in input().split(" ")]
print(convert_esm_into_year([e, s, m]))