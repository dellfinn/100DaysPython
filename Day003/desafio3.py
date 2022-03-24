# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if size == "S":
    valordaconta = 15
elif size == "M":
    valordaconta = 20
elif size == "L":
    valordaconta = 25
if add_pepperoni == "Y" and size == "S":
    valordaconta = valordaconta + 2
elif add_pepperoni == "Y" and size == "L" or add_pepperoni == "Y" and size == "M":
    valordaconta = valordaconta + 3
if extra_cheese == "Y":
    valordaconta = valordaconta + 1

print(f"Your final bill is: ${valordaconta}.")
