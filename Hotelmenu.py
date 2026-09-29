menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80,
}

print("WELCOME TO PYTHON RESTAURANT")
print("Pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 80\n")

order_total = 0

# First Item Order
item_1 = input("Enter the name of item you want to order = ").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available yet.")

# Second Item Order
another_order = input("\nDo you want to add another item? (Yes/No) ").capitalize()

if another_order == "Yes":
    item_2 = input(
        "Enter the name of second item = "
    ).title()  

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available!")

print(f"\nThe total amount of your order is Rs {order_total}")
