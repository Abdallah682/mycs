class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        elements_count = {}
        # iterating over the elements for frequency
        for element in arr:
        # checking whether it is in the dict or not
            if element in elements_count:
                # incerementing the count by 1
                elements_count[element] += 1
            else:
                # setting the count to 1
                elements_count[element] = 1
            # printing the elements frequencies
        lucky = -1
        for key, value in elements_count.items():
            print key ,value
            if key == value:
                if key>lucky:
                    lucky = key
        
        return lucky