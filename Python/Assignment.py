class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Country:", self.country)
        print("-" * 30)


person1 = Person("Ali", 22, "Pakistan")
person2 = Person("Sara", 25, "Canada")


person1.display_details()
person2.display_details()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect = Rectangle(5, 3)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.year} {self.make} {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display(self):
        super().display()
        print("Doors:", self.doors)


car = Car("Toyota", "Corolla", 2022, 4)
car.display()

class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


acc = BankAccount("12345", 1000)
acc.deposit(500)
acc.withdraw(300)
print("Final Balance:", acc.balance)


import math

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(4)
t = Triangle(6, 5)
print("Circle Area:", c.area())
print("Triangle Area:", t.area())


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, salary, department, bonus):
        super().__init__(name, salary)
        self.department = department
        self.bonus = bonus

    def annual_salary(self):
        return super().annual_salary() + self.bonus


m1 = Manager("Ali", 50000, "IT", 100000)
m2 = Manager("Sara", 60000, "HR", 120000)

print(m1.name, m1.annual_salary())
print(m2.name, m2.annual_salary())


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(self.title, self.author, self.year)


class Ebook(Book):
    def __init__(self, title, author, year, price):
        super().__init__(title, author, year)
        self.price = price

    def display(self):
        super().display()
        print("Price:", self.price)


e = Ebook("Python Basics", "John", 2023, 9.99)
e.display()


class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(self.sound)


class Dog(Animal):
    def __init__(self, color):
        super().__init__("Dog", "Bark")
        self.color = color

    def make_sound(self):
        print(f"{self.color} dog says {self.sound}")


d = Dog("Brown")
d.make_sound()

class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def remove_branch(self, branch):
        if branch in self.branches:
            self.branches.remove(branch)

    def display(self):
        print("Branches:", self.branches)


b = Bank("ABC Bank")
b.add_branch("Lahore")
b.add_branch("Karachi")
b.remove_branch("Lahore")
b.display()


class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity


class PersonalCareProduct(Product):
    def __init__(self, pid, name, price, warranty):
        super().__init__(pid, name, price)
        self.warranty = warranty

    def total_price(self, quantity):
        return super().total_price(quantity) + self.warranty * 10


p = PersonalCareProduct(1, "Hair Dryer", 2000, 2)
print("Total Price:", p.total_price(3))


class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt

    def transfer(self, other, amt):
        if amt <= self.balance:
            self.withdraw(amt)
            other.deposit(amt)


a1 = BankAccount("1", "Ali", 5000)
a2 = BankAccount("2", "Sara", 3000)

a1.transfer(a2, 1000)
print(a1.balance, a2.balance)


class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, dept):
        self.departments.append(dept)

    def remove_department(self, dept):
        if dept in self.departments:
            self.departments.remove(dept)

    def display(self):
        print("Departments:", self.departments)


u = University("Iqra University")
u.add_department("Computer Science")
u.add_department("Business")
u.remove_department("Business")
u.display()

