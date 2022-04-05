# def binn(arr, l, r, k):

#     while l <= r:
#         mid = l + (r - 1) // 2
#         if k == arr[mid]:
#             return mid
#         elif k > arr[mid]:
#             l = mid + 1
#         else:
#             r = mid - 1

#     return -1


data = [1, 2, 3, 4]
# print(binn(data, 0, len(data)-1, 4))

start = 0
end = len(data) - 1
pos = -1
key = 4

while start <= end:
    mid = (start + end) // 2

    if data[mid] == key:
        pos = mid
        break
    elif data[mid] < key:
        start = mid + 1
    else:
        end = mid - 1

if pos == -1:
    print("Not found")
else:
    print(pos)
