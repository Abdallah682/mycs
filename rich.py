class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ma=0
        for i in range(len(accounts)):
            summ=sum(accounts[i])
            if ma <summ:
                ma = summ
        return ma