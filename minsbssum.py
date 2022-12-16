class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        Sum, ans = 0, 0
        for ele in nums:
            Sum = Sum + ele
            ans = min(ans, Sum)
        return -ans + 1