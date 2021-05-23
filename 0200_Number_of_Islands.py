class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if either length is 0, there can't be any islands
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        island_count = 0

        # iterate over the whole grid
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                # if we detect a part of an island:
                if grid[m][n] == "1":
                    # increment the count and blow up the whole island
                    island_count += 1
                    Solution.deleteIsland(m, n, grid)

        return island_count


# recursive function to delete an island from the grid
# must only be called on indices within the grid
def deleteIsland(m, n, grid):
    # if this spot is land:
    if grid[m][n] == "1":
        # delete it
        grid[m][n] = "0"
        # and call the function again on every nearby position that is within the grid
        if 0 <= m - 1 < len(grid):
            Solution.deleteIsland(m - 1, n, grid)
        if 0 <= m + 1 < len(grid):
            Solution.deleteIsland(m + 1, n, grid)
        if 0 <= n - 1 < len(grid[0]):
            Solution.deleteIsland(m, n - 1, grid)
        if 0 <= n + 1 < len(grid[0]):
            Solution.deleteIsland(m, n + 1, grid)
