from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.dfs(1, k, n, [], res)
        return res

    def dfs(self, start, k, n, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start, n - (k - len(pre)) + 2):
            pre.append(i)
            self.dfs(i + 1, k, n, pre, res)
            pre.pop()
