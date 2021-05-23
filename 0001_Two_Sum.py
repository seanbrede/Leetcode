class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        # make table of {value: index} from the list of [index: value]
        table = collections.defaultdict(lambda: -1)
        for i in range(length):
            table[nums[i]] = i

        # for each index within nums:
        for i in range(length):
            # figure out the other number we need
            other_num = target - nums[i]

            # if that other number exists, and its index is different, return both indices
            if table[other_num] != -1 and table[other_num] != i:
                return [i, table[other_num]]
