class Solution:
    def numIslands(self, grid: []) -> int:

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1

        print(count)
        return count

    def dfs(self, grid, x, y):

        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]

        if grid[x][y] == "1":

            grid[x][y] = "v"

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (
                    nx >= 0
                    and nx < len(grid)
                    and ny >= 0
                    and ny < len(grid[0])
                    and grid[nx][ny] == "1"
                ):
                    self.dfs(grid, nx, ny)


Solution().numIslands(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
)

# expected : 3
