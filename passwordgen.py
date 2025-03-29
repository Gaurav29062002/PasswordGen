import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=""
sym=""
num=""
generate_password=""
for char in range(1,nr_letters+1):
    new_letters=random.choice(letters)
    password=password+new_letters
print(password)
for char in range(1,nr_symbols+1):
    new_sym=random.choice(symbols)
    sym=sym+new_sym
print(sym)
for char in range(1,nr_numbers+1):
    new_num=random.choice(numbers)
    num=num+new_num
print(num)
generate_password=generate_password+password+sym+num
print(generate_password)


#How to shuffle the passoword
print("Hard one")
mylist=[]
for char in range(0,nr_letters):
    mylist.append(random.choice(letters))

for char in range(0,nr_symbols):
    mylist.append(random.choice(symbols))

for char in range(0,nr_numbers):
    mylist.append(random.choice(numbers))
print("Before shuffling")
print(mylist)
print("After shuffle")
random.shuffle(mylist)
print(mylist)
final_password =""
for char in mylist:
    final_password+=char

print(f"Your Final Password is {final_password}")


