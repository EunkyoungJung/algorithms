'''
백준#2309
https://www.acmicpc.net/problem/2309
'''

'''
9개의 원소 중, 리스트 원소의 합이 100이 되는 7개의 원소를 찾는 문제
'''


def get_7_items_out_of_9_items_which_sum_is_100(items):
    '''
    9개 중 7개를 고르는 것은 9개 중 2개를 고르는 것과 같음
    9개 원소 중에 2개를 제거해서 원소의 합이 100이 되는 경우 찾기
    '''
    for x in range(0, len(items)-1):
        for y in range(1, len(items)):
            new_sum = sum(items) - (items[x] + items[y])
            if new_sum == 100:
                return list(filter(lambda item: item != items[x] and item != items[y], sorted(items)))


input_number = []
for _ in range(9):
    input_number.append(int(input()))

for number in get_7_items_out_of_9_items_which_sum_is_100(input_number):
    print(number)
