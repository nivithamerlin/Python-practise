'''Class & Objects

Create a class BankAccount with attributes: account_number, holder_name, balance.

Add methods to deposit, withdraw, and check balance.

Create multiple accounts and perform operations.'''

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.holder_name} : {self.account_number} who deposited {amount} and now balance is {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"{self.holder_name} : {self.account_number} who withdrawn {amount} and now balance is {self.balance}")
    def check_balance(self):
        print(f"{self.holder_name} balance is {self.balance}")
acc  = BankAccount(101, "Srisha")
acc.deposit(1500)
acc.withdraw(900)
acc.check_balance()

'''---Constructors (__init__)

Create a class Student with attributes: name, roll_no, marks.

Use __init__ to initialize values.

Write a method get_grade() that returns "Pass" if marks ≥ 50 else "Fail".'''

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def get_grade(self):
        if self.marks >= 50:
            return "Pass"
        else:
            return "Fail"
s1 = Student("daisy", 1, 99)
s2 = Student("raina", 2, 33)
print(f"{s1.name} : roll no {s1.roll_no} is {s1.get_grade()}")
print(f"{s2.name} : roll no {s2.roll_no} is {s2.get_grade()}")

''' ---Instance & Class Variables

Create a class Employee with attributes emp_id, name, salary.

Add a class variable company_name.

Show how changing company_name affects all employees.'''
class Employee:
    company_name = "Techcorp"
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def show_details(self):
        print(f"Id : {self.emp_id}, Name: {self.name}, Salary: {self.salary}, company: {self.company_name}")
e1 = Employee(101, "anusha", 20000)
e2 = Employee(102, "sreeja", 10000)
e1.show_details()
e2.show_details()
Employee.company_name = "hisha"
e1.show_details()
e2.show_details()

''' ---- Inheritance

Create a base class Vehicle with attributes brand and model.

Create subclasses Car and Bike.

Add methods like fuel_type() that prints "Petrol/Diesel/Electric".

Demonstrate inheritance by creating objects.'''

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_details(self):
        print(f"Brand name is {self.brand}, model is {self.model}")
class Car(Vehicle):
    def fuel_type(self):
        print(f"{self.brand} - {self.model} runs on petrol or diesel")
class Bike(Vehicle):
    def fuel_type(self):
        print(f"{self.brand} - {self.model} runs on petrol or electric")
c1 = Car("Toyota", "Innova")
c1.show_details()
c1.fuel_type()

b1 = Bike("yamaha", "R15")
b1.show_details()
b1.fuel_type()

''' ---- Encapsulation (Private Variables)

Create a class ATM with a private attribute __pin.

Add methods to set and verify PIN securely.

Show how direct access to __pin fails.'''
class ATM:
    def __init__(self):
        self.__pin = None
    def set_pin(self, pin):
        if(len(str(pin))) == 4:
            self.__pin = pin
            print("set succesfully")
        else:
            print("Invalid PIN, must have 4 digits")
    def verify_pin(self, pin):
        if self.__pin is None:
            print("No pin is set yet")
        elif self.__pin == pin:
            print("PIN verifies, you have access")
        else:
            print("Pin is Incorrect")
atm = ATM()
atm.set_pin(1234)
atm.verify_pin(2345)
print(atm.__pin)

'''---- Polymorphism

Create classes Dog and Cat with a method sound().

Dog → "Woof", Cat → "Meow".

Write a function animal_sound(animal) that takes any object and calls sound().'''
class Dog:
    def sound(self):
        return "Woof"
class Cat:
    def sound(self):
        return "meow"
def animal_sound(animal):
    print(animal.sound())
dog= Dog()
cat = Cat()
animal_sound(dog)
animal_sound(cat)

''' -----Abstraction

Use the abc module.

Create an abstract class Shape with abstract method area().

Implement subclasses Circle, Rectangle.

Each should calculate its own area.'''
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented
b1  = Book('Python basics', 200)
b2 = Book("oops in python", 600)
total_pages = b1 + b2
print("Total pages", total_pages)		

''' Operator Overloading

Create a class Book with attributes title, pages.

Overload the + operator to add total pages when two books are added.'''
class Library:
    def __init__(self):
        self.__books = []
    def add_book(self, title):
        if title not in self.__books:
            self.__books.append(title)
            print(f"{title} is added")
        else:
            print(f'{title} is already exists')
    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
            print(f"{title} is removed")
        else:
            print(f"{title} not found in library")
    def show_books(self):
        if self.__books:
            print("Books in library")
            for idx, book in enumerate(self.__books, start=1):
                print(f"{idx}. {book}")
        else:
            print("library is empty")
lib = Library()
lib.add_book("python basics")
lib.remove_book("datas")
lib.add_book("OOps")
lib.show_books()
lib.remove_book("OOps")
lib.show_books()

''' ----Advanced Real-Time

Design a class Ecommerce with attributes: cart (dictionary of items).

Methods: add_item(item, qty, price), remove_item(item), checkout().

Use OOP principles like encapsulation (private cart) and polymorphism (different payment methods like CreditCard, UPI).'''
from abc import ABC, abstractmethod
class Payment(ABC):
    def pay(self, amount):
        pass
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using creditcard")
class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI method")
class Ecommerce:
    def __init__(self):
        self.__cart = {}
    def add_item(self, item, qty, price):
        if item in self.__cart:
            self.__cart[item]['qty'] += qty
        else:
            self.__cart[item]= {'qty': qty, 'price': price}
        print(f"Added {qty} * {item} to cart")
    def remove_item(self, item):
        if item in self.__cart:
            del self.__cart[item]
            print(f"Removed {item} from cart")
        else:
            print(f"{item} not found in cart")
    def show_cart(self):
        if not self.__cart:
            print("Cart is empty")
        else:
            print("\n--- CART ITEMS ---")
            for item, details in self.__cart.items():
                print(f"{item}: {details['qty']} x ₹{details['price']} = ₹{details['qty']*details['price']}")
    def checkout(self, payment_method: Payment):
        total = sum(details['qty'] * details['price'] for details in self.__cart.values())
        if total == 0:
            print("Cart is empty. Cannot checkout.")
            return
        print(f"\nTotal Amount: ₹{total}")
        payment_method.pay(total)
        self.__cart.clear()   # Empty cart after payment
        print("Checkout Successful!")
shop = Ecommerce()

shop.add_item("Laptop", 1, 50000)
shop.add_item("Mouse", 2, 500)
shop.show_cart()

# Removing an item
shop.remove_item("Mouse")
shop.show_cart()

# Checkout using Credit Card
shop.checkout(CreditCard())

# Add again and pay via UPI
shop.add_item("Headphones", 1, 2000)
shop.show_cart()
shop.checkout(UPI())
