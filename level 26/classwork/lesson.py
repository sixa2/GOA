name = input("enter your name:")
print(name.capitalize())

#######################################
#######################################
#######################################

name = input("enter your name:")
print(name.upper())

#######################################
#######################################
#######################################

sentence = "my name is sixa i live in tbilisi"

print(sentence.count("i"))

#######################################
#######################################
#######################################


sentence = "my name is sixa i live in tbilisi"

print(sentence.find("i"))

#######################################
#######################################
#######################################

sentence = "my name is sixa i live in tbilisi"

print(sentence.index("a"))

#######################################
#######################################
#######################################

email = []

ans = int(input("how many emails you want to add:"))

for i in range(ans):
    answer = input("add email:")

    if answer.endwith("@gmail.com"):
        email.append(answer)
        print("email is correct!")
    else:
        print("email is incorrect!")

