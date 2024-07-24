def odd_index_sum(num):
    total = 0
    for i in range(len(num)):
        if i % 2 == 1:
            total += num[i]
    return total


num = [1, 2, 3, 4, 5, 6]
result = odd_index_sum(num)
print(result)
