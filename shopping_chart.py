
# Creat a shooping chart that will continously ask the user for a food product and the price of that product
# Have an exit clause if the user wishes to stop adding more things to their cart
# At the end show the food items and the toatl cost to the user

foods =[]
prices =[]
total = 0

while True:
    foods=input("Enter a food to buy or press q to quit")
    if foods.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {foods}:R"))
        foods.append(foods)
        prices.append(price)
        
print("-----YOUR CART-----")

for food in foods:
    print(food, end= "")
    
for price in prices:
    total += price
print("\n")           
print(F"Your total is:R{total}")        
        
        