def numbers_comparision (a,b,c):
    if a==b==c:
        return False
    if a > b and a > c:
        if b > c:
            return a, a-c