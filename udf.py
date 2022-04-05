# str = "HelloHe"

# index = -1
# for i in range(len(str)):
#     if str[i] not in str[i + 1:] and str[i] not in str[0:i]:
#         index = i
#         break


# print(index)


# lst = [1, 6, 4, 2, 7, 3, 10]


# def findMissingPositive(arr, size):
#     for i in range(size):
#         if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0):
#             arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

#     for i in range(size):
#         if (arr[i] > 0):

#             return i + 1
#     return size + 1


# print(findMissingPositive(lst, len(lst)))

# num = int(input(("Enter number: ")))


# if num not in range(-2147483647, 2147483647):
#     print("Invalid number")
# else:
#     rever = 0
#     while num != 0:
#         digit = num % 10
#         rever = rever * 10 + digit
#         num //= 10

#     index = -1
#     rever = str(rever)
#     if rever.startswith("0"):
#         for i in range(len(rever)):
#             if rever[i] != 0:
#                 index = i
#                 break
#         rever = rever[index:]
#         print(f"rever Number: {int(rever)}")
#     else:
#         print(f"rever Number: {int(rever)}")

# x = 90

# def func():
#     print(x)

# func()
