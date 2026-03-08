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

from typing import List 

def maximumWealth(accounts: List[List[int]]) -> int:
    max_wealth = 0
    for customer in accounts:
        currect_customer_wealth = 0

        for bank in customer:
            currect_customer_wealth += bank

        max_wealth = max(max_wealth, currect_customer_wealth)

    return max_wealth


accounts = [[1,2,3],[3,2,1]]

print(maximumWealth(accounts))
