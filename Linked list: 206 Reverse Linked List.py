# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        previous = None
        #双指针, 注意previous points to None!
        current = head
		# 过一遍linked list, while current loop
        while current:
			# store the next value that will be changed in temp, same logic as swap function, DO NOT store & swap current node
            tmp = current.next
			#swap current value with the next position value
            current.next = previous
			#然后2指针都到下一个继续loop
            previous = current
            current = tmp
        return previous	
