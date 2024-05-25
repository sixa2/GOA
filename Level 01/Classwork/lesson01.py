name = "Dato"
# name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "Gabriel" არის ცვლადისთვის მნიშვნელობა
surname = "Sikharulidze"

print(name)
# პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

# name = "Dato" # ეს არის str(string) ტიპის ცვლადი
# სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები
age = 18 # ეს არის int(integer) მთელი რიცხვი
height = 1.70 # ეს არის float ტიპის ცვლადი (ათწილადი)

knows_programming = True # True ან False, Boolean ტიპის ცვლადი

print(name + " " + surname)

# print(type(age)) # age გადაეცა type ფუნქციას, რომელმაც დააბრუნა მისი ტიპი
# და დაბრუნებული ნებისმიერი სიტყვა დავპრინტეთ, რომელმაც გაგვაგებინა რომ
# print(type(age)) - ის ტიპი არის int(integer) (მთელი რიცხვი)

print(type(age))
print(type(name))
print(type(surname))
print(type(height))
print(type(knows_programming))
