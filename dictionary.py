# # marks = int(input("Enter your marks: "))

# # if marks >= 90 and marks <= 100:
# #     grade = "A"
# # elif marks >= 80 and marks < 90:
# #     grade = "B"
# # elif marks >= 70 and marks < 80:
# #     grade = "C"
# # elif marks >= 60 and marks < 70:
# #     grade = "D"
# # else:
# #     grade = "F"

# # print(f"Grade = {grade}")

# # set_elem = input("Enter eleemnts of sets: ")
# # set_elem = set(set_elem.split(" "))
# # print(set_elem)

# m_elems = input("Enter number of elements in m: ")
# m = input(f"Enter {m_elems} numbers separated by space: ")

# n_elems = input("Enter number of elements in n: ")
# n = input(f"Enter {n_elems} numbers separated by space: ")
# m = set(m.split(" "))
# n = set(n.split(" "))

# differ = m.symmetric_difference(n)
# differ = list(differ)

# differ.sort()
# print(differ)

my_items = {
    "mobile": 2111,
    "laptop": 1000,
    "power-bank": 111
}

new_dic = {}

for key, value in my_items.items():
    new_dic[value] = key

print(new_dic)
