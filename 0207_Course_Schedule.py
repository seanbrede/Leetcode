class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # has any DFS seen this node?
        v_ever = [False] * numCourses
        # has the current DFS seen this node?
        v_curr = [False] * numCourses

        # create a dict of adjacency for fast access
        adj_table = collections.defaultdict(list)
        for a_i, b_i in prerequisites:
            if a_i == b_i: return False
            adj_table[b_i].append(a_i)

        # for each node:
        for node in range(numCourses):
            # if we haven't ever visited that node:
            if v_ever[node] == False:
                # do DFS from that node
                cycle, v_ever = Solution.recursiveDFS(node, v_ever, v_curr, adj_table)
                # if we found any cycle, end by returning false
                if cycle == True:
                    return False

        # will only get here if there's no cycle
        return True

    def recursiveDFS(node, v_ever, v_curr, adj_table):
        # mark this node as visited in both senses
        v_ever[node] = True
        v_curr_next = copy.deepcopy(v_curr)
        v_curr_next[node] = True

        # for each neighbor of this node:
        for neighbor in adj_table[node]:
            # if we've visited it before in this DFS, CYCLE FOUND!
            if v_curr[neighbor] == True:
                return True, v_ever

            # if we've seen the neighbor in a previous DFS, we know there's no cycle
            # because we would have found it already
            if v_ever[neighbor] == True:
                continue

            # else, visit it and do DFS from it
            cycle, v_ever = Solution.recursiveDFS(neighbor, v_ever, v_curr_next, adj_table)
            if cycle == True:
                return True, v_ever

        return False, v_ever
