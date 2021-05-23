class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        # first, sort the intervals by start time
        intervals = sorted(intervals, key=lambda x: x[0])

        for inter in intervals:
            # if the current interval begins before the last merged one ends
            # then they overlap, so merge them by changing the end
            if merged and inter[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], inter[1])
            # otherwise they don't overlap, just add the current interval
            else:
                merged.append(inter)

        return merged
