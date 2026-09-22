#
# @lc app=leetcode id=82 lang=python3
# @lcpr version=30404
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # if head is None:
        #     return None
        # dummy = ListNode()
        # dummy.next = head
        # fast = head
        # slow = head
        # count = 0
        # pre = dummy
        # while slow is not None:
        #     count = 0
        #     while fast is not None and fast.val == slow.val:
        #         count+=1
        #         fast = fast.next
        #     if count > 1:
        #         pre.next = fast
        #     if count == 1:
        #         pre = slow
        #     slow = fast
        # return dummy.next


        # dummyUniq = ListNode(101)
        # dummyDup = ListNode(101)

        # pUniq, pDup = dummyUniq, dummyDup
        # p = head

        # while p is not None:
        #     if (p.next is not None and p.val == p.next.val) or p.val == pDup.val:
        #         # 发现重复节点，接到重复链表后面
        #         pDup.next = p
        #         pDup = pDup.next
        #     else:
        #         # 不是重复节点，接到不重复链表后面
        #         pUniq.next = p
        #         pUniq = pUniq.next

        #     p = p.next
        #     # 将原链表和新链表断开
        #     pUniq.next = None
        #     pDup.next = None

        # return dummyUniq.next


        # base case
        if head is None or head.next is None:
            return head
        if head.val != head.next.val:
            # 如果头结点和身后节点的值不同，则对之后的链表去重即可
            head.next = self.deleteDuplicates(head.next)
            return head
        # 如果如果头结点和身后节点的值相同，则说明从 head 开始存在若干重复节点
        # 越过重复节点，找到 head 之后那个不重复的节点
        while head.next is not None and head.val == head.next.val:
            head = head.next
        # 直接返回那个不重复节点开头的链表的去重结果，就把重复节点删掉了
        return self.deleteDuplicates(head.next)
# @lc code=end



#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#

