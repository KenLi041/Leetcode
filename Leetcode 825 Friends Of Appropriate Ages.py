class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        i = 0
        size = len(ages)
        
        left = 0; right = 0; res = 0
        ages.sort()

        for i in ages: 
            if i <= 14:
                continue
            while left < size and (0.5*i+7 >= ages[left]):
                left += 1
            while right < size and ages[right] <= i:
                right += 1
            res += (right-left)
        return res
