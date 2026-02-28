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

val = np.full(10,5)

for i in val:
    print(i, end=" ")
