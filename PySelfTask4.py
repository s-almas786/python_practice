# def isPalindrome(st: str) -> bool:
#     if st == st[::-1]:
#         return True
#     else:
#         return False

# print(isPalindrome("abaa"))

# def find_first_upper(st, current):
#     end = len(st)

#     if st[current].isupper():
#         return current
#     elif current < end:
#         return find_first_upper(st, current+1)
#     else:
#         return -1

# def findMax(A, n):
#     if (n == 1):
#         return A[0]
#     return max(A[n - 1], findMax(A, n - 1))

# print(findMax([2, 3, 1, 0, 4], 5))


# def anagramCheck2(str1, str2):
#     list1 = list(str1)
#     list2 = list(str2)
#     list1.sort()
#     list2.sort()

#     position = 0
#     matches = True

#     while position < len(str1) and matches:
#         if list1[position] == list2[position]:
#             position = position + 1
#         else:
#             matches = False

#     return matches


# print(anagramCheck2('python', 'ythonp'))
