class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        if numRows >= 1: triangle.append([1])
        if numRows >= 2: triangle.append([1, 1])

        for i in range(3, numRows + 1):
            new_row = [(triangle[len(triangle) - 1][j - 1] + triangle[len(triangle) - 1][j]) for j in range(1, i - 1)]
            new_row = [1] + new_row + [1]
            triangle.append(new_row)

        return triangle
