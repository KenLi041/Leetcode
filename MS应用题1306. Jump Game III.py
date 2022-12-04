class Solution:
    #Given arr, 一开始在start index of the array. When you are at index i, 可左右跳到跨度为i位置value的跨度 i + arr[i] or i - arr[i], 到value 0才return true.
    #如Input: arr = [4,2,3,0,3,1,2], start = 5, All possible ways to reach at index 3 with value 0 are: index 5 (value = 1)-> index 4 (value = 3) -> index 1 (value = 2) -> index 3 (0, stop), or index 5 -> index 6 -> index 4 -> index 1 -> index 3 
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set() #store value that's visited to compare later
        def Recursion(i):
            if i < 0 or i >= len(arr): #if value is negative or value不能大于array length要不然就跳出去了out of range, so false
                return False
            if arr[i] == 0: #value是0了就到了
                return True
            if i in visited: #Don't go to visited node values
                return False
            visited.add(i) #add the visited value
            index1 = i - arr[i] #2种情况往左或往右跳都要check
            index2 = i + arr[i]
            return Recursion(index1) or Recursion(index2)
        return Recursion(start)
