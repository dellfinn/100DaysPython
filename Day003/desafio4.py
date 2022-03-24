# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if size == "S":
    valordaconta = 15.00
elif size == "M":
    valordaconta = 20.00
elif size == "L":
    valordaconta = 25.00
if add_pepperoni == "Y" and size == "S":
    valordaconta = valordaconta + 2
elif add_pepperoni == "Y" and size == "L" or add_pepperoni == "Y" and size == "M":
    valordaconta = valordaconta + 3
if extra_cheese == "Y":
    valordaconta = valordaconta + 1

print(f"Your final bill is: ${valordaconta}.")
