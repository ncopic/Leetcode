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
        #--------------------------------------------------------
        # Solution 1 - build linked list backwards, then reverse
        #--------------------------------------------------------

        '''
        #Deals with empty list1 or list2
        if (list1 == None) and (list2 == None):
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        #assuming list1 and list2 are populated with 1+ elements:
        reverse_out_list = ListNode(next=None)        
        while((list1 != None) or (list2 != None)):
            
            if (list1 == None):
                reverse_out_list = ListNode(val=list2.val, next=reverse_out_list)
                list2 = list2.next
            elif (list2 == None):
                reverse_out_list = ListNode(val=list1.val, next=reverse_out_list)
                list1 = list1.next
            elif list1.val <= list2.val:
                reverse_out_list = ListNode(val=list1.val, next=reverse_out_list)
                list1 = list1.next
            else:
                reverse_out_list = ListNode(val=list2.val, next=reverse_out_list)
                list2 = list2.next
        
        out_list = False
        while(reverse_out_list.next != None):
            if out_list:
                out_list = ListNode(val=reverse_out_list.val, next=out_list)
                reverse_out_list = reverse_out_list.next
            else:
                out_list = ListNode(val=reverse_out_list.val, next=None)
                reverse_out_list = reverse_out_list.next
        print(out_list)
        return out_list
        '''
        

        #--------------------------------------------------------
        # Solution 2 - take inputs, convert to array, then put back into ListNode form -slow, but it works
        #--------------------------------------------------------

        '''
        #quick return statment for empty lists
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        #initalize output variables
        out_list = ListNode(next=None)
        ol = []

        #Converting linked list into array
        l1 = []
        while list1 != None:
            l1.append(list1.val)
            list1 = list1.next

        l2 = []
        while list2 != None:
            l2.append(list2.val)
            list2 = list2.next
        
        #manipulating input arrays into 1 single sorted array
        while (len(l1) != 0) or (len(l2) != 0):

            if len(l1) == 0:
                ol.append(l2[-1])
                l2.pop()
            elif len(l2) == 0:
                ol.append(l1[-1])
                l1.pop()
            elif l1[-1] >= l2[-1]:
                ol.append(l1[-1])
                l1.pop()
            else: #l2[-1] > l1[-1]
                ol.append(l2[-1])
                l2.pop()

        #taking sorted array and putting back into linked list form
        while len(ol) != 0: 
            if len(ol) == 1:
                out_list.val = ol[0]
                ol.pop(0)  
            else:
                out_list.val = ol[0]
                ol.pop(0)
                out_list = ListNode(next=out_list)
        return out_list
        
        '''



        #--------------------------------------------------------
        # Solution 3 - keep LL notation; use PREV,HEAD,NEXT
        #--------------------------------------------------------
        
        if (list1 == None) and (list2 == None):
            return None
        if (list1 == None):
            return list2
        if (list2 == None):
            return list1

        l1_head = list1
        l2_head = list2

        '''
        #Accidentially rebuilt a backwards linked-list...
        out_list = False
        while l1_head or l2_head:
            if l1_head == None:
                if out_list:
                    out_list = ListNode(l2_head.val, next=out_list)
                    l2_head = l2_head.next
                else:
                    out_list = ListNode(l2_head.val, next=None)
                    l2_head = l2_head.next
            elif l2_head == None:
                if out_list:
                    out_list = ListNode(l1_head.val, next=out_list)
                    l1_head = l1_head.next
                else:
                    out_list = ListNode(l1_head.val, next=None)
                    l1_head = l1_head.next
            elif l1_head.val <= l2_head.val:
                if out_list:
                    out_list = ListNode(l1_head.val, next=out_list)
                    l1_head = l1_head.next
                else:
                    out_list = ListNode(l1_head.val, next=None)
                    l1_head = l1_head.next
            else:
                if out_list:
                    out_list = ListNode(l2_head.val, next=out_list)
                    l2_head = l2_head.next
                else:
                    out_list = ListNode(l2_head.val, next=None)
                    l2_head = l2_head.next
        print(out_list)
        return out_list
        '''

        out_list = ListNode()
        while (l1_head) or (l2_head):
            if l1_head == None:
                out_list.next = ListNode(l2_head.val, next=None)
                l2_head = l2_head.next
            elif l2_head == None:
                out_list.next = ListNode(l1_head.val, next=None)
                l1_head = l1_head.next
            elif l1_head.val >= l2_head.val:
                out_list.next = ListNode(l1_head.val, next=None)
                l1_head = l1_head.next
            else:
                out_list.next = ListNode(l2_head.val, next=None)
                l2_head = l2_head.next
        print(out_list)
        return out_list
        