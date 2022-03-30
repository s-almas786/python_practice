# for i in range(6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print(" ")

# bubble sort

# arr = [5, 1, 4, 2, 8]
# data = [-2, 45, 0, 11, -9]


# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


# def selection_sort(arr):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]


# # selection_sort(data)
# bubble_sort(data)
# print(data)

# even = list(range(2, 11, 2))
# print(even)

# l = [(value, value**2) for value in range(4)]

# print(l)

# users = ["ahmab", "usman", "ab", "ali"]
# new_users = [user for user in users if user.endswith("ab")]
# print(new_users)

# matrix = [
#     [1, 2, 3, 4],
#     [3, 4, 5, 8],
#     [7, 66, 43, 33, 90, 22]
# ]

# new_arr = []
# for row in matrix:
#     for col in row:
#         new_arr.append(col)

# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         new_arr.append(matrix[row][col])

# new_arr = [value for row in matrix for value in row]
# print(new_arr)

# transpose

# transpose = []

# for i in range(len(matrix[0])):
#     transpose_row = []
#     for row in matrix:
#         transpose_row.append(row[i])
#     transpose.append(transpose_row)

# transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# # print(transpose)

# n = [[value+1 for value in row] for row in matrix]
# print(n)

# {key, value for item in iterable}

prices = {
    "laptop": 10000,
    "mobile": 5000,
    "power": -999,
}
# new_dic = {value: key for key, value in prices.items()}

# for key, value in dict

# new_dic = {}

# for i in range(3):
#     new_dic[i] = "Usama"

# print(new_dic)

# new_dic = {i: "Usama" for i in range(3)}
# print(new_dic)

# new_prices = {k: v*2 for k, v in prices.items()}
# print(new_prices)

# prices_five = {k: 0 if v < 0 else v for k, v in prices.items()}
# print(prices_five)
# prices_five = {k: v for k, v in prices.items() if v > 5000}
# print(prices_five)
