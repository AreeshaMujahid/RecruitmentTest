# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#inorder to create linked list 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#inorder to print linked list
def printList(node: ListNode):
    while node is not None:
        print(str(node.val), end=" ")
        node = node.next
    print()

#inorder to Remove Nth Node From End of List
class Solution:
    def removeNthFromEnd(self,head: ListNode, n: int) -> ListNode:
        
        slow = head                                             #the first will point to the head of the linked list     
        fast = head                                             #the second will point to the Nth node from the beginning.
        
        
        # Move fast pointer n steps ahead
        for i in range(0, n):                                   
            if fast.next is None:                              # If n is equal to the number of nodes, delete the head node
                if i == n - 1:
                    head = head.next
                return head
            fast = fast.next

                                    
        while fast.next is not None:                          # Loop until fast node reaches to the end
            slow = slow.next                                  # Now we will move both slow and fast pointers
            fast = fast.next
            
        # Delink the nth node from last
        if slow.next is not None:
            slow.next = slow.next.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    c=Solution()
    printList(c.removeNthFromEnd(head, 2))

    head = ListNode(1)
    #printList(removeNthFromEnd(head, 1))

    head = ListNode(1)
    head.next = ListNode(2)
    c=Solution()
    #printList(c.removeNthFromEnd(head, 1))

        
