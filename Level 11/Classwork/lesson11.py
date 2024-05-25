# მომხმარებელი შემოიტანს რიცხვს 1-10 მდე, თუ რიცხვი იქნება 5 გამოვუტანოთ
# რომ მოიგო, თუ რიცხვი იქნება 9 გამოვუტანოთ რომ ნახევარი პრიზი მოიგო, 
# ხოლო ყველა სხვა დანარჩენ შემთხვევაში გამოვუტანოთ, რომ წააგო

number = int(input("Enter a number between 1-10: "))
if number == 5:
    print("You won a prize")
elif number == 9:
    print("You won half of a prize")
else:
    print("L")