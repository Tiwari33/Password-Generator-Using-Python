import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["0","1","2","3","4","5","6","7","8","9","10"]
symbols=["!","*","&","#","@","$","_"]
nr_letter=random.randint(8,10)
nr_number=random.randint(2,4)
nr_symbols=random.randint(2,4)
password_list=[]
for char in range(nr_letter):
    password_list.append(random.choice(letters))
for num in range(nr_number):
    password_list+=(random.choice(numbers))
for symb in range(nr_symbols):
    password_list+=(random.choice(symbols))
    
random.shuffle(password_list)

password=""
for char in password_list:
    password+=char

    
"".join(password)
print(password)

    
    

    
