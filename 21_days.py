#Find the Duplicate Number
def findDuplicate(nums):
    temp, temp1 = 0, 0
    while True:
        temp = nums[temp]
        temp1 = nums[nums[temp1]]
        if temp == temp1:
            break
    
    temp2 = 0
    while True:
        temp = nums[temp]
        temp2 = nums[temp2]
        if temp == temp2:
            return temp


#Diameter of Binary Tree
def diameterOfBinaryTree(self, root):
    res = [0]
    
    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0], 2 + left + right)
        
        return 1 + max(left, right)
    
    dfs(root)
    return res[0]

#Maximum Depth of Binary Tree
def maxDepth(self, root):
    if not root:
        return 0
    
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Invert Binary Tree
def invertTree(self, root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    
    self.invertTree(root.left)
    self.invertTree(root.right)        
    
    return root

#Top K Frequent Elements
def topKFrequent(self, nums, k):
    if len(nums) == 1:
        return [nums[0]]

    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    h = []
    from heapq import heappush, heappop
    for key in d: #
        heappush(h, (d[key], key)) 
        if len(h) > k:
            heappop(h)

    res = []
    while h: 
        frq, item = heappop(h)
        res.append(item)
    return res

#Remove Nth Node From End of List
def removeNthFromEnd(self, head, n):
    temp = head
    temp1 = head
    
    for _ in range(n):
        temp = temp.next
        
    if not temp:
        return head.next
    
    while temp.next:
        temp1 = temp1.next
        temp = temp.next
    temp1.next = temp1.next.next
    return head

#Same Tree
def isSameTree(self, p, q):   
    if not p and not q:
        return True

    if not q or not p:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left) 

#Last Stone Weight
import heapq
class Solution:
    def lastStoneWeight(self, A):
        h = [-x for x in A]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]

#Add two numbers
def addTwoNumbers(self, l1, l2):
    res = dummy = ListNode()
    carry = 0
    while l1 or l2:
        v1, v2 = 0, 0
        if l1: v1, l1 = l1.val, l1.next
        if l2: v2, l2 = l2.val, l2.next
        
        val = carry + v1 + v2
        res.next = ListNode(val%10)
        res, carry = res.next, val//10
        
    if carry:
        res.next = ListNode(carry)
        
    return dummy.next

#Reverse Linked List II
def reverseBetween(self, head, left, right):
    if not head:
        return None

    while left != right and left<right:
        left_node = right_node = head 

        for _ in range(1, left):
            left_node=left_node.next
        
        for _ in range(1, right):
            right_node = right_node.next

        left_node.val, right_node.val = right_node.val, left_node.val

        left += 1
        right -= 1

    return head

#Swapping Nodes in a Linked List
def swapNodes(self, head, k):

    first = last =  head
    temp = head
    
    for _ in range(1,k):
        first = first.next
        
    i = 0
    while temp.next:
        i += 1
        temp = temp.next
    
    for _ in range(i-k+1):
        last = last.next
        
    first.val, last.val = last.val, first.val
    return head

# Reverse Linked List

def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """       
    temp_pre = None
    
    while head:
        temp_post = head.next
        head.next = temp_pre

        temp_pre = head
        head = temp_post
        
    return temp_pre


# Permutations
def permute(self, nums):
    res = []
    
    if (len(nums) == 1):    
        return [nums[:]]
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = self.permute(nums)
        
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
        
    return res

# Letter Combinations of a Phone Number
def letterCombinations(self, digits):
    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    
    result = []
    
    def backtracking(i, curStr):
        if len(curStr) == len(digits):
            result.append(curStr)                
            return 
        for c in dic[digits[i]]:
            backtracking(i+1, curStr + c)
            
    if digits:
        backtracking(0, "")
            
    return result     