class Solution(object):
    def transpose(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0])
        return [[A[i][j] for i in range(m)] for j in range(n)]