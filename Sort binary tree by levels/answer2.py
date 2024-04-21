from collections import deque
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if node is None:
        return None
    res = []
    q = deque()
    q.append(node)
    while q:
        q_len = len(q)
        for i in range(q_len):
            node = q.popleft()
            if node:
                res.append(node.value)
                q.append(node.left)
                q.append(node.right)
    return res