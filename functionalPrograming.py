# data = [['ABC', 12, 3, 100],
#         ['DEF', 10, 5, 1000],
#         ['GHI', 13, 9, 200]]

# data.sort(key=lambda row: (row[2], row[3]))

# print(data)

# Selection sort using for loop
def selectio_sort_for(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]


def selectio_sort_while(arr):
    i = 0
    while i < len(arr):
        min = i
        j = i + 1

        while j < len(arr):
            if arr[min] > arr[j]:
                min = j
            j += 1

        arr[i], arr[min] = arr[min], arr[i]
        i += 1


def insertion_sort_for(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


def insertion_sort_while(arr):
    i = 1
    while i < len(arr):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
        i += 1


def bubble_sort_for(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]


def bubble_sort_while(arr):
    i = 0

    while i < len(arr):
        j = 0

        while j < len(arr) - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1


data = [9, 5, 1, 0, 3, 99]
print(data)
# selectio_sort_for(data)
# selectio_sort_while(data)
# insertion_sort_for(data)
# insertion_sort_while(data)
# bubble_sort_for(data)
bubble_sort_while(data)
print(data)
