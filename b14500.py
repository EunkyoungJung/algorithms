"""
백준#14500
https://www.acmicpc.net/problem/14500
"""

"""
각 셀에 숫자가 써져 있는 사각형 판에
5개 모양의 테트리스 조각 중 1개를 놓았을 때
테트리스 조각 밑의 숫자들의 합이 제일 큰 경우를 찾는 문제

테트리스 조각별로 90도씩 회전을 해서 놓을 수 있는 모든 경우의 수를 구한다
"""

BLOCK_SHAPES = (
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    # ()[][][]
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    # ()
    # []
    # []
    # []
    ((0, 0), (1, 0), (1, 1), (1, 2)),
    # ()
    # [][][]
    ((0, 0), (0, 1), (1, 0), (2, 0)),
    # ()[]
    # []
    # []
    ((0, 0), (0, 1), (0, 2), (1, 2)),
    # ()[][]
    #     []
    ((0, 0), (1, 0), (2, 0), (2, -1)),
    #   []
    #   []
    # ()[]
    ((0, 0), (0, 1), (0, 2), (-1, 2)),
    #     []
    # ()[][]
    ((0, 0), (1, 0), (2, 0), (2, 1)),
    # ()
    # []
    # [] []
    ((0, 0), (0, 1), (0, 2), (1, 0)),
    # ()[][]
    # []
    ((0, 0), (0, 1), (1, 1), (2, 1)),
    # ()[]
    #   []
    #   []
    ((0, 0), (0, 1), (1, 0), (1, 1)),
    # ()[]
    # [][]
    ((0, 0), (0, 1), (-1, 1), (-1, 2)),
    #   [][]
    # ()[]
    ((0, 0), (1, 0), (1, 1), (2, 1)),
    # ()
    # [][]
    #   []
    ((0, 0), (0, 1), (1, 1), (1, 2)),
    # ()[]
    #   [][]
    ((0, 0), (1, 0), (1, -1), (2, -1)),
    #   ()
    # [][]
    # []
    ((0, 0), (0, 1), (0, 2), (-1, 1)),
    #   []
    # ()[][]
    ((0, 0), (0, 1), (0, 2), (1, 1)),
    # ()[][]
    #   []
    ((0, 0), (1, 0), (2, 0), (1, 1)),
    # ()
    # [][]
    # []
    ((0, 0), (1, 0), (2, 0), (1, -1)),
    #   ()
    # [][]
    #   []
)


def get_max_score(row_count, col_count, board_point_map):
    max_block_score = 0
    for i in range(row_count):
        for j in range(col_count):

            # 블럭별로 판에 끼우면서 점수 계산
            for block in BLOCK_SHAPES:
                is_fit_in_board = True

                block_score = 0
                for dx, dy in block:
                    x, y = i + dx, j + dy
                    # 해당 블럭이 판 안에 존재하는 지 체크
                    if 0 <= x < row_count and 0 <= y < col_count:
                        block_score += board_point_map[x][y]
                    else:
                        is_fit_in_board = False
                        break

                if is_fit_in_board and max_block_score < block_score:
                    max_block_score = block_score

    return max_block_score


def read_input():
    row_count, col_count = map(int, input().split())
    point_map = [list(map(int, input().split())) for _ in range(row_count)]
    return [row_count, col_count, point_map]


def solve():
    row_count, col_count, board_point_map = read_input()
    print(get_max_score(row_count, col_count, board_point_map))


solve()
