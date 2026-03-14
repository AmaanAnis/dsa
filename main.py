# a = [
#     "amaan",
#     "bashar",
#     "sami",
#     "mohammad",
#     "ahmed",
#     "ali",
#     "hassan",
#     "omar",
#     "yousef",
#     "khaled",
#     "abdullah",
# ]


# def filter_words(list_of_words):
#     list_of_a_words = list_of_words
#     a_words = []
#     other_words = []
#     for a in list_of_a_words:
#         if a.startswith("a"):
#             # if a[0] == "a":
#             a_words.append(a)
#         else:
#             other_words.append(a)

#     return a_words, other_words


# print(filter_words(a))


# n=5
# for i in range(0, n/2):
#     print(i)

# n = 5
# u_n = n // 2
# print(u_n)
# m = 10

# for i in range(0, n):
#     for j in range(0, m):
#         for k in range(0, n):
#             print(f"hello {i} {j} {k}")

import numpy as np

# val = np.linspace(10, 20, 5)

# val = np.arange(10, 20, 5)

# val = np.logspace(10, 20, 5)

# val = np.zeros(10)

# val = np.ones(10)

# val = np.full(10,5)

# for i in val:
#     print(i, end=" ")

# zero_dim = np.array(10)
# print(zero_dim)

# one_dim = np.array([1,2,3,4,5,6])
# print(one_dim)

# two_dim = np.array([[1,2,3], [4,5,6], [6,7,8]])
# print(two_dim)

# three_dim = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(three_dim)

# def insert_in_min(self, value, x):
#     t = self.head
#     while(t.next != None):
#         if(t.data == x):
#             break
#         t = t.next

#     temp = Node(value)

#     temp.prev = x.next
#     temp.next


# def runningSum(nums):
#     for i in nums:
#         i = 1
#         nums[i] += nums[i - 1]

#     return nums


# nums = [1, 2, 3, 4]
# runningSum(nums)

# from typing import List

# def maximumWealth(accounts: List[List[int]]) -> int:
#     max_wealth = 0
#     for customer in accounts:
#         currect_customer_wealth = 0

#         for bank in customer:
#             currect_customer_wealth += bank

#         max_wealth = max(max_wealth, currect_customer_wealth)

#     return max_wealth


# accounts = [[1,2,3],[3,2,1]]

# print(maximumWealth(accounts))

# from typing import List


# def fizzBuzz(n: int) -> List[str]:
#     answer = []
#     for i in range(1, n + 1):
#         divisible_by_3 = i % 3 == 0
#         divisible_by_5 = i % 5 == 0
#         if divisible_by_3 and divisible_by_5:
#             answer.append("FizzBuzz")
#         elif divisible_by_3:
#             answer.append("Fizz")
#         elif divisible_by_5:
#             answer.append("Buzz")
#         else:
#             answer.append(str(i))
#     return answer


# n = 3
# fizzBuzz(n)


# def numberOfSteps(num: int) -> int:
#     result = 0
#     while num > 0:
#         is_even = num % 2 == 0
#         if is_even:
#             num /= 2
#         else:
#             num -= 1
#         result += 1
#     return result

# print(numberOfSteps(14))

# from typing import Optional


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         middle = head
#         end = head
#         while end != None and end.next != None:
#             middle = middle.next
#             end = end.next.next

#         return middle


# BST 
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
    if(root == None):
        return Node(value)
    if(root.data == value):
        return value
    if(root.data > value):
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if(root == None):
        print("Element not found", end='\n')
        return
    if(root.data == value):
        print("Element found", end='\n')
        return
    if(root.data > value):
        search(root.left, value)
    else:
        search(root.right, value)
    
def get_successor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root

def delete(root, value):
    if(root == None):
        return root
    if(root.data > value):
        root.left = delete(root.left, value)
    elif(root.data < value):
        root.right = delete(root.right, value)
    else:
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = delete(root.right, succ.data)
    return root

def in_order(root):
    if(root != None):
        in_order(root.left)
        print(root.data, end=' ')
        in_order(root.right)

# root = Node(20)
# root.left = Node(15) 
# root.right = Node(30) 
# root.left.left = Node(12) 
# root.left.right = Node(18)

root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)
in_order(root)
print("\n")
# search(root, 90)
# print("\n")
# search(root, 20)
# print("\n")
delete(root, 20)
print("\n")
in_order(root)