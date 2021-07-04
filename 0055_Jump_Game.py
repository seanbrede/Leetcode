class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        steps_left = 0
        i = 0

        # while we are within the array and still have steps left
        while i < last_pos:
            # update the number of steps left, if none then quit
            steps_left = max(nums[i], steps_left)
            if steps_left == 0: return False

            # update our position and reduce the number of steps left
            steps_left -= 1
            i += 1

        # we only get here if we reached the end
        return True
