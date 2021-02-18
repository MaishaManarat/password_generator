 #Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#one way
random_letters = ''.join(random.choices(letters, k = nr_letters))

random_symbols = ''.join(random.choices(symbols, k = nr_symbols))

random_number = ''.join(random.choices(numbers, k = nr_numbers))

ran = random_letters+random_symbols+random_number
length = len(ran)

final_random = ''.join(random.sample(ran, k = length))


print(f"Your generated password is: {final_random}")


#another way

random_l = ""

for l in range (1, nr_letters+1):
  l = random.choice(letters)
  random_l = l + random_l


random_s = ""

for s in range (1, nr_symbols+1):
  s = random.choice(symbols)
  random_s = s + random_s


random_n = ""
for n in range (1, nr_numbers+1):
  n = random.choice(numbers)
  random_n = n + random_n


r = random_l + random_s +random_n
password_list = list(r)
random.shuffle(password_list)



password = ""

for i in password_list:
  password = i + password

print(f"Your generated password is: {password}")
