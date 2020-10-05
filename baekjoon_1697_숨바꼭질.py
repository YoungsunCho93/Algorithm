# BFS

from collections import deque

n, k = map(int, input().split())

visit = [0] * 100001

queue = deque()

t = 0

while True:
    if len(queue) > 0:
        (n, t) = queue.popleft()
    if n == k:
        break
    if (n - 1) >= 0 and visit[n - 1] == 0:
        visit[n - 1] = 1
        queue.append((n - 1, t + 1))
    if (n + 1) <= 100000 and visit[n + 1] == 0:
        visit[n + 1] = 1
        queue.append((n + 1, t + 1))
    if (n * 2) <= 100000 and visit[n * 2] == 0:
        visit[n * 2] = 1
        queue.append((n * 2, t + 1))

print(t)

# 5 17

# expect: 4