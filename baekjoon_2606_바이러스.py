def dfs(x):
    visit.add(x)
    for i in list(graph[x]):
        if i not in list(visit):
            visit.add(i)
            dfs(i)


total = int(input())
n = int(input())

for i in range(total + 1):
    graph[i] = set()

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visit = set([1])
graph = {}

dfs(1)

print(len(visit) - 1)

# input
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
