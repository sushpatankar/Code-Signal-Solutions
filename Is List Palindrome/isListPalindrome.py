# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    if l is None:
        return True
    n = l
    out = []
    while n is not None:
        out.append(n.value)
        n = n.next
    return out == out[::-1]
