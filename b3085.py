"""
백준#3085
https://www.acmicpc.net/problem/3085
"""

"""
인접한 위치에 가장 많이 같은 색상이 연달이 연달아 있는 경우를 찾는 문제
"""


def get_max_adjacent_redundant_color_count(color_map):
    """
    2차원 색깔 배열에서 연달아 인접하는 중복된 컬러의 최대 개수(result)를 리턴하는 함수
    1. 중복된 컬러의 최대 개수(result)를 1로 초기화 한다. (한 셀의 컬러는 최소한 1개임으로)
    2. 행을 순차적으로 순회하여 인접하는 중복된 컬러의 개수를 센다.
    2-.1 해당 행의 중복된 컬러의 개수가 현재까지 찾은 가장 큰 값이라면 result 값을 변경한다.
    3. 열을 순차적으로 순회하여 인접하는 중복된 컬러의 개수를 센다.
    3-.1 해당 열의 중복된 컬러의 개수가 현재까지 찾은 가장 큰 값이라면 result 값을 변경한다.
    4. 연달아 인접하는 중복된 컬러의 최대 개수(result)를 리턴한다.
    """
    result = 1
    row_count = len(color_map)
    col_count = len(color_map[0])

    for i in range(row_count):
        # 같은 행에서 인접한 값 비교
        color_count = 1
        for j in range(1, col_count):
            # 이전 값과 현재 값이 동일한지 체크
            if color_map[i][j] == color_map[i][j-1]:
                color_count += 1
            else:
                # 연달아 같지 않으면 다시 1로 초기화
                color_count = 1

            # result값 업데이트
            if result < color_count:
                result = color_count

        # 같은 열에서 인접한 값 비교
        color_count = 1
        for j in range(1, col_count):
            if color_map[j][i] == color_map[j-1][i]:
                color_count += 1
            else:
                color_count = 1

            # result값 업데이트
            if result < color_count:
                result = color_count

    return result

color_map = []
n = int(input())
for _ in range(n):
    color_map.append([x for x in input()])

result = 0
"""
1. result를 0으로 초기화한다.
2. 행을 순회하면서 행의 j번째와 j+1번째를 교환한다.
2-1. 변경된 컬러맵에서 '연달아 인접하는 중복된 컬러의 최대 개수'가 result 보다 크다면 result를 변경한다.
2-2. 2-1의 변경을 원복한다. (행의 j+1번째와 j번째를 교환한다)
3. 열을 순회하면서 행의 i번째와 i+1번째를 교환한다.
3-1. 변경된 컬러맵에서 '연달아 인접하는 중복된 컬러의 최대 개수'가 result 보다 크다면 result를 변경한다.
3-2. 3-1의 변경을 원복한다. (열의 i+1번째와 i번째를 교환한다)
4. result를 출력한다.
"""
for i in range(n):
    for j in range(n):
        if j+1 < n:
            # 행 안에서 옆으로 비교
            color_map[i][j], color_map[i][j + 1] = color_map[i][j + 1], color_map[i][j]
            max_redundant_color_count = get_max_adjacent_redundant_color_count(color_map)
            if result < max_redundant_color_count:
                result = max_redundant_color_count
            color_map[i][j], color_map[i][j + 1] = color_map[i][j + 1], color_map[i][j]
        if i+1 < n:
            # 열 안에서 위아래로 비교
            color_map[i][j], color_map[i + 1][j] = color_map[i + 1][j], color_map[i][j]
            max_redundant_color_count = get_max_adjacent_redundant_color_count(color_map)
            if result < max_redundant_color_count:
                result = max_redundant_color_count
            color_map[i][j], color_map[i + 1][j] = color_map[i + 1][j], color_map[i][j]

print(result)
