class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #double pointer problem
        nums_len = len(nums) #get array length 
        if nums_len <= 2: #if less than 2 elements directly return
            return nums_len
        pointer_slow = 2 #start slow pointer at 2nd element
        for pointer_fast in range(2, nums_len): #fast pointer iterate and compare with slow pointer
            if not ( (nums[pointer_fast] == nums[pointer_slow-1]) and (nums[pointer_fast] == nums[pointer_slow-2]) ):
                nums[pointer_slow] = nums[pointer_fast]
                pointer_slow += 1
        return pointer_slow
