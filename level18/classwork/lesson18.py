# #1.
# num = []
# for i in range(1, 11):
#     num.append(i)

# count = len(num)
# print("სია შედგება {count} ელემენტისგან: {num}")

# #2.
# num1 = int(input("first num: "))
# num2 = int(input("second num: "))

# numbers = []
# for i in range(num1, num2 + 1):
#     numbers.append(i)
# total_sum = sum(numbers)
# print(f"numbers from {num1}  to {num2}  {numbers}")
# print(f"sum: {total_sum}")


def calculate_and_print():
    start = int(input("first num: "))
    end = int(input("second num: "))

    numbers = []
    for num in range(start, end + 1):
        numbers.append(num)

    max_num = max(numbers)
    min_num = min(numbers)
    sum_nums = sum(numbers)

    print(f"numbers from {start}  to {end}:  {numbers}")
    print(f"max: {max_num}")
    print(f"min: {min_num}")
    print(f"sum: {sum_nums}")

calculate_and_print()
