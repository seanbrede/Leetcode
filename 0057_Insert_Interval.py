class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval[0], newInterval[1]
        left, right = [], []

        # for each interval:
        for inter in intervals:
            # if that interval ends before the new one starts, put it on the left side
            if inter[1] < new_start:
                left.append(inter)

            # if the new one ends before that interval starts, put it on the right side
            elif new_end < inter[0]:
                right.append(inter)

            # otherwise, they overlap somewhere:
            else:
                # combine this interval with the new one by taking the min of the starting times
                new_start = min(new_start, inter[0])
                # and the max of the ending times
                new_end = max(new_end, inter[1])

        # now put the whole thing together
        inserted = left + [[new_start, new_end]] + right

        return inserted
