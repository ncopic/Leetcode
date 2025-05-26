# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        print(list2.val)
        l1_curr = list1.val
        l1_next = list1.next
        l2_curr = list2.val
        l2_next = list2.next 
        out_list = ListNode()
        
        out_list.val = l1_curr
        out_list.next = l1_next
        print(out_list)
        #if l1_curr > l2_curr:

