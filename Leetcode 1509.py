class Solution:
    def minDifference(self, nums: List[int]) -> int:
        minlist = []
        maxlist = []
             #first we create lists for min and max
            
        if not len(nums) > 4: #we can see the pattern that if delete 1 element we consider 2 possibility: biggest-2nd smallest or 2nd biggest-smallest. Therefore for array length x we consider x+1 possibilities so all nums with 4 or less digits can just change to all the same number so only need to consider array length>4
            return 0
            
            
        
        for digit in nums: #get 2 heaps to get the min and max digits in
            heappush(minlist, -digit)
            if len(minlist)==5: #shouldn't take more than 4 digits in!
                heappop(minlist)
            heappush(maxlist, digit)
            if len(maxlist)==5:
                heappop(maxlist)
                
                
        maxlist.sort() #sort min and max
        minlist = list(sorted([-count for count in minlist]))
        
        return min((maxlist[0]-minlist[0]), #return the min out of the x+1 possibilities, in this case 4
                   (maxlist[1]-minlist[1]),
                   (maxlist[2]-minlist[2]),
                   (maxlist[3]-minlist[3]))
