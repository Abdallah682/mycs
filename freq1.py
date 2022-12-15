class Solution(object):
    def containsDuplicate(self, nums):

        elements_count = {}
        for element in nums:
            if element in elements_count:
                return True
            else:
                elements_count[element] = 1
        return False