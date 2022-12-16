class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fr=max(nums)-1
        nums.remove(max(nums))
        return fr * (max(nums)-1)