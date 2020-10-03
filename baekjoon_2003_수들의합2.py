# Two Pointers Algorithm

n, target = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = 0

sum = array[0]

count = 0

while True:

    if sum < target:
        end += 1
        sum += array[end]

    elif sum > target:
        sum -= array[start]
        start += 1

    else:
        count += 1
        sum -= array[start]
        start += 1

    print(start, end, sum)

    if end == (len(array) - 1) and sum < target:
        break

print(count)

# 4 2
# 1 1 1 1