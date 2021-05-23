"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # empty graph should return an empty graph
        if not node: return None

        # table of {val: Node} for determining if a node has already been cloned
        node_table = collections.defaultdict(lambda: Node(val=0))

        # call recursive function for cloning the graph and return the result
        new_graph, _ = Solution.cloneNodes(node, node_table)
        return new_graph

    # recursive function to find nodes and clone them
    def cloneNodes(node, node_table):
        # make a new node with the same value as the original node and add it to the table
        new_node = Node(val=node.val, neighbors=[])
        node_table[node.val] = new_node

        # for each neighbor of the original node:
        for n in node.neighbors:
            # if that neighbor doesn't exist in the table, clone the neighbor and add it to the table
            if node_table[n.val].val == 0:
                new_neighbor, node_table = Solution.cloneNodes(n, node_table)

            # add the cloned node as a neighbor
            new_node.neighbors.append(node_table[n.val])

        # return the new node and the update seen set
        return new_node, node_table
