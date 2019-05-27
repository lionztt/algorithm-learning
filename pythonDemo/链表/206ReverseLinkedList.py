# 206 链表反转
# python 中以面向对象的方式实现链表，链表节点为对象实例
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 创建链表
def createLinkedList(arr, n):
    if n == 0:
        return None
    head = ListNode(arr[0])
    curNode = head
    for i in range(1, len(arr)):
        next=ListNode(arr[i])
        curNode.next = next
        curNode = curNode.next
    return head


# 打印链表
def printLinkedList(head: ListNode):
    curNode = head
    while curNode:
        print(curNode.val, '->', end=' ')
        curNode = curNode.next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None  # cur前一个指针
        while head:
            next = head.next  # cur下一个指针
            head.next = pre
            pre = head
            head = next
        return pre

    # python简单写法
    def reverseList2(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            pre, pre.next, cur = cur, pre, cur.next
        return pre

arr = [1, 2, 3, 4, 5]
head = createLinkedList(arr, 5)
printLinkedList(head)
print("\n")
result=Solution()
last =result.reverseList(head)
printLinkedList(last)
