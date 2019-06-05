class Solution(object):
    def uniquePathsWithObstacles(self, d):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        a = len(d)
        b = len(d[0])
        if a == 0 or b == 0:
            return 0
        d[0][0] ^= 1
        for i in range(1, b):
            d[0][i] = d[0][i - 1] & (d[0][i] ^ 1)
        for i in range(1, a):
            d[i][0] = d[i - 1][0] & (d[i][0] ^ 1)
        for i in range(1, a):
            for j in range(1, b):
                d[i][j] = (d[i - 1][j] + d[i][j - 1]) if d[i][j] == 0 else 0
        return d[a - 1][b - 1]
