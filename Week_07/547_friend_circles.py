class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        f = {}
        s = {}
        count = len(M)

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            nonlocal count
            x_father, y_father = find(x), find(y)
            if x_father == y_father: return
            if s.setdefault(x_father, 1) < s.setdefault(y_father, 1):
                f[x_father] = y_father
                s[y_father] += s[x_father]
            else:
                f[y_father] = x_father
                s[x_father] += s[y_father]
            count -= 1

        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    union(i, j)
        return count