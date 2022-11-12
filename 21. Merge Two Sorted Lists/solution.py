# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sort(self, list: ListNode, comp: ListNode):
        if not list.next:
            list.next = comp
            return
        else:
            if list.next.val <= comp.val:
                self.sort(list.next, comp)
            else:
                newComp = list.next
                list.next = comp
                self.sort(list.next, newComp)
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            out = list1
            self.sort(list1, list2)
        else:
            out = list2
            self.sort(list2, list1)
            
        return out