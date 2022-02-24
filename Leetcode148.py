# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temporary, answer = [], []
        while head:
            temporary.append(head.val) #Only given the head, must first take all values out to an array 
            head = head.next #go to next value
        for i in sorted(temporary): #then sort the array to ascending order
            currentnode = ListNode(i) #start node by node
            answer.append(currentnode) #put the right values 
        for i in range(len(answer)-1):
            answer[i].next = answer[i+1] #go to next node to put next value
        if len(answer) == 0: #if empty array
            return None
        else: return answer[0] #return answer array values
