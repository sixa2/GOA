# def are_distinct(a, b, c):
#     if a == b:
#         return False
#     if a == c:
#         return False
#     if b == c:
#         return False
#     return True


def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  
    
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    
    return second

