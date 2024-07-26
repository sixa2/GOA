
family_members = ["mari", "tika", "mimi", "ebi"]
for member in family_members:
    print(member)




numbers = list(range(1, 11))
print("First element:", numbers[0])
print("Last element:", numbers[-1])


   

numbers = list(range(10, 21))
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers[i] += 1
print("Modified list:", numbers)





first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
location = input("Enter your current location: ")
email = input("Enter your email: ")
user_info = [first_name, last_name, age, location, email]
print("information:", user_info)





last_name = "Smith"
for i in range(len(last_name)):
    print(last_name[i])
