class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        steps_left = 0
        i = 0

        # while we are within the array and still have steps left
        while i < last_pos:
            steps_left = max(nums[i], steps_left)
            if steps_left == 0: return False

            steps_left -= 1
            i += 1

        return True
