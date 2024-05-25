# num = int(input("Enter a number: "))
# if num < 0:
#     print("Negative number")
# elif num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Error")

################################################

# for num in range(2, 21,):
#     if num % 2 == 0:
#         print(f"{num} even")
#     else:
#         print(f"{num} odd")

################################################

# result = 0

# user_input = int(input("Enter a number: "))
# user_input1 = int(input("Enter a second number: "))

# result = user_input + user_input1
# print(result)

################################################

# user_pin = int(input("Enter PIN: "))
# if user_pin == 1121:
#     print("Withdrawal: ")
#     print("Deposit: ")
#     print("Balance: ")
# else:
#     print("Get lost")

################################################

# user_input = input("Enter username: ")
# user_input1 = input("Enter a password: ")
# if user_input == "admin" and user_input1 == "password123":
#     print("Login Successful")
# else:
#     print("Password or username is incorrect")

#################################################

user_input = int(input("Enter your age: "))
if user_input <= 13:
    print("You are a child")
elif user_input <= 21:
    print("You are a teenager")
else:
    print("You old as hell")