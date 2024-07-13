
for number in range(21):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")



number = int(input("შეიტანეთ რიცხვი: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")



print("20-მდე ლუწი რიცხვები:")
for number in range(0, 21, 2):
    print(number)
 


sum = 0
for number in range(50, 101):
    sum += number

print("50-დან 100-მდე ყველა რიცხვის ჯამი:", sum)




word = "marshals"

print("Word printed backwards:")
for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")



