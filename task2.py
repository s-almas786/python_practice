# Task 01

data = ["NY", "FL", "CA", "VT"]

new_data = {value: value for value in data}

print(new_data)

# Task 02

# numbers = [value for value in range(100, 161, 10)]
number_dict = {value: value / 100 for value in range(100, 161, 10)}
print(number_dict)


# Task 03
users = []

size = int(input("Enter number of users: "))

i = 0

while i < size:
    user = input("Enter user: ")

    try:
        if not(user.isalpha()):
            raise Exception("Username cannot contain numbers")
            break
        else:
            users.append(user)
    except Exception:
        raise

    i += 1

print(users)
