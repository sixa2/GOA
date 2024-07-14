def my_function(number, times):
    return number * times

result = my_function(5, 5)
print(result)

################################################
################################################
################################################

def my_function(string):
    
    return len(string)

result =my_function(["ola", "alo"])
print(result)

################################################
################################################
################################################

def my_function(number, num):
    return number * num

result = my_function(1, 5)
print(result)

################################################
################################################
################################################

def my_function(strings):
    list = []
    for i in strings:
        list.append(len(i))
    return list
result = my_function(["bruh", "dude","negga"])
print(result)

################################################
################################################
################################################

def my_function(string):
    if string == string[::-1]:
        return True
    else:
        return False
result = my_function(input("enter :"))
print(result)

################################################
################################################
################################################

# def sport list(list):
list = ["rugby", "bodybuilding" , "football",]
max = len(list[0])

for i in list:
   list.append(len(i))

   