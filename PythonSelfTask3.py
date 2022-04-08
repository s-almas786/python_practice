def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)


num = int(input("Enter a number: "))

if num < 0:
    print("Negative numbers donot have factorial")
else:
    print(f"Factorial of {num} is {fact(num)}")


# def binary(arr, left, right, key):
#     if left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             return binary(arr, mid+1, right, key)
#         else:
#             return binary(arr, left, mid-1, key)

#     return -1


# data = [1, 2, 3, 4, 5]
# result = binary(data, 0, len(data)-1, 50)

# if result == -1:
#     print("Required element not exist in list")
# else:
#     print(f"Required element is at index {result}")
