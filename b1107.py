"""
백준#1107
https://www.acmicpc.net/problem/1107
"""

"""
100부터 특정채널까지 도달하는 가장 빠른 방법 구하는 문제
문제에서 고장난 숫자버튼을 알려줌
1. 특정채널에 가장 가까운 숫자 구하기(멀쩡한 버튼(0~9 중에서 고장난 숫자버튼 제외한 나머지)을 가지고 만들 수 있는)
2. 1번에서 구한 숫자에서 +/-버튼을 눌러서 특정 채널 도달하기
"""


def get_number_button_press_count(target_channel_number, number_buttons):
    current_number = target_channel_number

    while current_number >= 0:
        # 각 자리수가 누를 수 있는 번호인지 체크
        digit = current_number % 10
        if number_buttons[digit] is False:
            return 0

        # 오른쪽으로 한자리 쉬프트
        current_number //= 10

        if current_number == 0:
            break

    return len(str(target_channel_number))


def get_updown_button_press_count(target, source):
    return abs(target - source)


def solve_problem():
    START_CHANNEL = 100
    broken_button_numbers = []
    number_buttons = [True] * len(range(0, 10))

    target_channel = int(input())
    broken_number_button_count = int(input())

    if broken_number_button_count > 0:
        broken_button_numbers = list(map(int, input().split()))

    for button_number in broken_button_numbers:
        number_buttons[button_number] = False

    # 숫자버튼을 누르지 않고 업다운 버튼으로 이동하여 target_channel로 도달한 경우의 값으로 초기화
    min_press_count = get_updown_button_press_count(START_CHANNEL, target_channel)
    for channel in range(0, max(START_CHANNEL * 2, target_channel * 2)):
        number_button_press_count = get_number_button_press_count(channel, number_buttons)

        if number_button_press_count > 0:
            new_press_count = number_button_press_count + get_updown_button_press_count(target_channel, channel)
            min_press_count = min(min_press_count, new_press_count)

    print(min_press_count)


solve_problem()