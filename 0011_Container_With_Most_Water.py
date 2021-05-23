class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        best_area = 0

        while i < j:
            smaller_height = min(height[i], height[j])

            # calculate the current area and update if it's better
            curr_area = smaller_height * (j - i)
            best_area = max(best_area, curr_area)

            # move each pointer over while its height is worse
            while (height[i] <= smaller_height and i < j): i += 1
            while (height[j] <= smaller_height and i < j): j -= 1

        return best_area
