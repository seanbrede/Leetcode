class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        # create grids of reachability for both oceans
        p_reachable = [[False for _ in range(cols)] for _ in range(rows)]
        a_reachable = [[False for _ in range(cols)] for _ in range(rows)]

        # run the DFS from each tile next to an ocean
        for r in range(rows):
            recursiveDFS(r, 0, heights, p_reachable)
            recursiveDFS(r, cols - 1, heights, a_reachable)
        for c in range(cols):
            recursiveDFS(0, c, heights, p_reachable)
            recursiveDFS(rows - 1, c, heights, a_reachable)

        # harvest all coordinates in the reachability grid for which both oceans are reachable
        coords = []
        for r in range(rows):
            for c in range(cols):
                if p_reachable[r][c] and a_reachable[r][c]:
                    coords.append([r, c])

        return coords


def recursiveDFS(r, c, heights, o_reachable):
    rows, cols = len(heights), len(heights[0])

    # set this cell as being reachable from this ocean
    o_reachable[r][c] = True

    # recursively call this method on each surrounding cell if:
    #   1. that cell is within the array
    #   2. that cell's height is at least as large as this cell's
    #   3. that cell has not already been marked as reachable
    if 0 <= r + 1 < rows and heights[r + 1][c] >= heights[r][c] and not o_reachable[r + 1][c]:
        recursiveDFS(r + 1, c, heights, o_reachable)
    if 0 <= r - 1 < rows and heights[r - 1][c] >= heights[r][c] and not o_reachable[r - 1][c]:
        recursiveDFS(r - 1, c, heights, o_reachable)
    if 0 <= c + 1 < cols and heights[r][c + 1] >= heights[r][c] and not o_reachable[r][c + 1]:
        recursiveDFS(r, c + 1, heights, o_reachable)
    if 0 <= c - 1 < cols and heights[r][c - 1] >= heights[r][c] and not o_reachable[r][c - 1]:
        recursiveDFS(r, c - 1, heights, o_reachable)
