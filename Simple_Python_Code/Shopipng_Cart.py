foods = []
prices = []
total = 0

while True:
    food = input("What type of food do you want? ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"What is the price of the {food}? "))
        foods.append(food)
        prices.append(price)
print("------YOUR CART------")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Your total is : {total}")