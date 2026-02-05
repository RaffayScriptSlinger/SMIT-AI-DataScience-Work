# Here Can I Do My Python revision

name = "Raffay"

print("My Name Is " , name)


num = float(1)
num2 = 2.3
num3 = True

print(type(num))
print(type(num2))
print(type(num3))

# Type Casting and Basic Variable has been Practiced

print(4 + 9)
print(4-9)
print(4*4)
print(4 / 4)

UserAge = int(input("Enter Your Age "))

if (UserAge >= 18):
    Gender = input("Are You male or female if male so type m if not so type f : ")
    if Gender == "M" or Gender == "m" :
        print("Go In Male Voting station")
    elif Gender == "F" or Gender == "f":
        print("Go in Female oting Station")
    else:
        print("There Is an Error")
    print("You are Eligible For Voting")
elif(UserAge < 18):
    print("You are not eligible for voting")
else:
    print("I thing There Is an error")

# Conditions And Nested Condition Will End Here

for i in range(10):
    print(i)


name = input("Enter Your Name")
   

while name != "Raffay" :
    print("Enter Name Again")
    name =  input("Enter Your Name")


for i in range(11):
    print(i)
    if i == 6:
        break


# Loops are End here and break and continue statement has been checked


myName = "Raffay"

print(myName[0:3])

print(myName.isupper())

print(myName.count("a"))


lst = [1,2,3,4,5]


tup = (1,2,3,4,5)

my_Set = {1,2,3,4,5}

lst.append(6)
tup.index(1)
my_Set.add(88)
print(lst)
print(tup)
print(my_Set)


my_Dict = [
   {
    "id"  : 1,
   " name" : "Raffay"
   },
   {
       "id" : 2,
       "name" : "Shayan"
   }
]

print(my_Dict[0].keys())

print(my_Dict[1]["name"])


def myName(name = "Raffay"):
    return name

myName()


def greet(name = "Guest"):
    print("Welcome" + name)


greet()


def info(userName , age):
    print(userName , age)

info(age=23,userName="Shayan")


try:
    num = int(input("Number: "))
    result = 10 / num
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Zero divide nahi kar sakte!")
