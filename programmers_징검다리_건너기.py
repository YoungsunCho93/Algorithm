# https://tech.kakao.com/2020/04/01/2019-internship-test/
# Binary Search
# => O(nlogm), n = len(stones), m = max(stones)


def checkStone(stones, mid, k):
    count = 0
    check = True
    for i in stones:
        if i - mid > 0:
            count = 0
        else:
            count += 1

        if count >= k:
            check = False
            break

    return check


def solution(stones, k):

    left = 1
    right = max(stones)

    while left <= right:
        mid = (right + left) // 2

        stoneCheck = checkStone(stones, mid, k)

        if stoneCheck:
            left = mid + 1
        else:
            right = mid - 1

    return left


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

# expected : 3