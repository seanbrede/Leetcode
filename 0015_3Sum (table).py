class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # get nums in sorted order
        nums.sort()

        no_duplicates = set()

        for i, first_val in enumerate(nums[:-2]):
            # if the first value is a duplicate of the previous, go to the next first value
            if i >= 1 and first_val == nums[i-1]:
                continue

            table = {}
            for second_val in nums[i+1:]:
                if second_val not in table:
                    table[-first_val-second_val] = 1
                else:
                    no_duplicates.add((first_val, -first_val-second_val, second_val))

        return map(list, no_duplicates)
