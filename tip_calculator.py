intro = """\nWelcome to tip calculator\n
Calculate your order and tip\n"""
print(intro)

def calculator():
    dishes = (int(input("Enter the amount of dishes: ")))
    food_price =  (float(input("Enter the price of the meal: ")))
    tip = (int(input("Enter the tip percentage without a symbol: ")))

    if dishes > 0:
        total_food = round((dishes * food_price), 2) 
        recompense = round(((tip * total_food) / 100), 2)
        print(f'The price of the {dishes} dishes is: {total_food}$ and the tip by shipment is: {recompense}$')

if __name__ == "__main__":
    calculator()
