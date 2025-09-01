# Find difference between two lists
list1 = [1, 2, 3, 4]
list2 = [2, 4, 6]
set1 = set(list1)
set2 = set(list2)
diff1 = list(set1 - set2)
diff2 = list(set2 - set1)
print(diff1)
print(diff2)

# Find common elements between two lists
list1 = [1, 2, 3, 4]
list2 = [2, 4, 6]
set1 = set(list1)
set2 = set(list2)
common = list(set1.intersection(set2))
print(common)

# print diagonal of matrix 
matrix = [
    [1, 2, 3],   # row 0
    [4, 5, 6],   # row 1
    [7, 8, 9]    # row 2
]
for i in range(3):
    print(matrix[i][i])
for i in range(3):
    print(matrix[i][2 - i])

# fancy numbers available pgm
user_input = input("enter the value: ")
print("user number is", user_input)
count = 0
for i in range(9000000000, 9999999999):
    if str(user_input) in str(i):
        print("available num are:", str(i))
        count += 1
        if count >= 10:
            break

# count the word in string and store it in dictionary
log = "error failed error success failed error"
output = {}
for word in log.split():
    if word in output:
        output[word] += 1
    else:
        output[word] = 1
print(output)

#  filter out of stock
products = [{"item": "Pen", "stock": 10}, {"item": "Pencil", "stock": 0}, {"item": "Eraser", "stock": 5}]
out_of_stock = {}
for thing in products:
     if thing["stock"] <= 0:
          out_of_stock[thing["item"]] = thing["stock"]
print(out_of_stock)

# loop through and find the amount greater than 200 
orders = [{"order_id": 1, "amount": 250}, {"order_id": 2, "amount": 1000}, {"order_id": 3, "amount": 150}]


output = []

for order in orders:
    if order["amount"] > 200:
        output.append(order)

print(output)

# Separate Even/Odd Employee IDs
employee_ids = [101, 204, 305, 406]
list1 = []
list2 = []

for emp in employee_ids:
    if emp % 2 == 0:
        list1.append(emp)
    if emp % 3 == 0:
        list2.append(emp)

print("Divisible by 2:", list1)
print("Divisible by 3:", list2)


# print maximum stock among all
inventory = [{"item": "Notebook", "stock": 10}, {"item": "Marker", "stock": 50}, {"item": "Scale", "stock": 30}]
max_stock = inventory[0]
for invent in inventory[1:]:
    if invent["stock"] > max_stock["stock"]:
        max_stock = invent
print(max_stock)

# count vowels in sentence
sentence = "Python is a great language"
vowels = ["a", "e", "i", "o", "u"]
count = 0
for sent in sentence.lower():
    if sent in vowels:
        count += 1
print(count)

# group by first letter in dictionary
words = ["apple", "ant", "banana", "bat", "cat"]
grouped = {}
for word in words:
    first_letter = word[0]
    if first_letter not in grouped:
        grouped[first_letter] = []
    grouped[first_letter].append(word)
print(grouped)

# filter products with price less than 100
products = [{"item": "Pen", "price": 50}, {"item": "Notebook", "price": 120}, {"item": "Eraser", "price": 20}]
new_product = []
for prod in products:
    if prod["price"] < 100:
        new_product.append(prod)
print(new_product)

# how many times each fruit appears
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = {}
for fruit in fruits:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1
print(count)

# list name of students who scored more than 75
students = [{"name": "Ram", "score": 65}, {"name": "Meena", "score": 85}, {"name": "Raj", "score": 90}]
scored = []
for stud in students:
    if stud["score"] > 75:
        scored.append(stud["name"])
        
print(scored)

# get a list of all even numbers
numbers = [10, 15, 21, 24, 30]
even_num = []
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)
print(even_num)

# find total stock from list of products
items = [{"item": "Pen", "stock": 10}, {"item": "Pencil", "stock": 5}, {"item": "Eraser", "stock": 8}]
total = 0
for i in items:
    total += i["stock"]
print(total)

# find items that are out of stock
inventory = [{"item": "Pen", "stock": 10}, {"item": "Pencil", "stock": 0}, {"item": "Notebook", "stock": 0}]

out_of_stock = []
for invent in inventory:
    if invent["stock"] == 0:
        out_of_stock.append(invent["item"])
        
print(out_of_stock)

# filter books published after 2010
books = [{"title": "Book A", "year": 2005}, {"title": "Book B", "year": 2015}, {"title": "Book C", "year": 2020}]
final = []
for book in books:
    if book["year"] > 2010:
        final.append(book["title"])
print(final)

# find the sum of expense
expenses = [{"day": "Mon", "amount": 200}, {"day": "Tue", "amount": 150}, {"day": "Wed", "amount": 300}]
sum = 0
for exp in expenses:
    sum += exp["amount"]
print(sum)

# count each word
word = "Hello world Hello python"
new = word.split()
print(new)
count = 0
my_dict = {}
for w in new:
    if w in my_dict:
        my_dict[w] +=1
    else:
        my_dict[w] = 1
print(my_dict)












