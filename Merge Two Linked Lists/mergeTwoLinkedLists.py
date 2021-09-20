# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    def add_toList(l1):
        out = []
        while l1!=None:
            out.append(l1.value)
            l1 = l1.next
        return out
    list1 = add_toList(l1)
    list2 = add_toList(l2)
    return sorted(list1+list2)

