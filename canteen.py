import datetime

# CANTEEN MENU (CATEGORY-WISE)

menu = {
    "Snacks": {
        "Burger": 80,
        "Pizza": 150,
        "Momos": 60,
        "French Fries": 50
    },
    "Drinks": {
        "Cold Coffee": 70,
        "Tea": 15,
        "Lassi": 40
    },
    "Meals": {
        "Veg Thali": 120,
        "Fried Rice": 90,
        "Paneer Roll": 70
    }
}

cart = []

# SHOW MENU FUNCTION

def show_menu():
    print("\n======= FULL MENU =======")
    for category, items in menu.items():
        print(f"\n--- {category} ---")
        for item, price in items.items():
            print(f"{item} : ₹{price}")
    print("==========================\n")


# ADD ITEM TO CART FUNCTION

def add_to_cart():
    show_menu()
    category = input("Enter category: ").title()

    if category not in menu:
        print("Category not found!")
        return

    item = input("Enter item name: ").title()

    if item not in menu[category]:
        print("Item not found in this category!")
        return

    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("Quantity must be positive!")
            return
    except ValueError:
        print("Invalid quantity!")
        return

    cart.append((item, qty, menu[category][item]))
    print(f"Added {qty} x {item} to cart!\n")


# GENERATE BILL FUNCTION

def generate_bill():
    if not cart:
        print("No items in cart! Add something first.")
        return

    print("\n=========== BILL ===========")
    total = 0

    for item, qty, price in cart:
        cost = qty * price
        total += cost
        print(f"{item} ({qty} x ₹{price}) = ₹{cost}")

    discount = 0
    if total >= 500:
        discount = total * 0.10
    elif total >= 300:
        discount = total * 0.05

    final_total = total - discount

    print("-----------------------------")
    print(f"Subtotal: ₹{total}")
    print(f"Discount: ₹{discount}")
    print(f"FINAL TOTAL: ₹{final_total}")
    print("=============================\n")

    save_bill(final_total)


# SAVE BILL TO FILE

def save_bill(amount):
    now = datetime.datetime.now()
    with open("bill.txt", "a") as f:
        f.write(f"Date: {now}\n")
        for item, qty, price in cart:
            f.write(f"{item} - Qty: {qty} - Price: ₹{price}\n")
        f.write(f"Total Amount: ₹{amount}\n")
        f.write("------------------------------\n")

    print("Bill saved to bill.txt\n")


# ADMIN MODE

def admin_mode():
    print("\n--- ADMIN PANEL ---")
    password = input("Enter admin password: ")

    if password != "admin123":
        print("Incorrect password!")
        return

    print("\n1. Add Menu Item\n2. Remove Menu Item")
    choice = input("Choose option: ")

    if choice == "1":
        cat = input("Enter category: ").title()
        item = input("Enter new item name: ").title()
        price = int(input("Enter price: "))

        if cat in menu:
            menu[cat][item] = price
        else:
            menu[cat] = {item: price}

        print(f"Item {item} added to {cat}!")

    elif choice == "2":
        cat = input("Enter category: ").title()
        item = input("Enter item name to remove: ").title()

        if cat in menu and item in menu[cat]:
            del menu[cat][item]
            print(f"Removed {item} from {cat}")
        else:
            print("Item not found!")


# MAIN LOOP

def main():
    while True:
        print("\n===== CANTEEN SYSTEM =====")
        print("1. Show Menu")
        print("2. Add Item to Cart")
        print("3. Generate Bill")
        print("4. Admin Mode")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            generate_bill()
        elif choice == "4":
            admin_mode()
        elif choice == "5":
            print("Thank you! Visit again")
            break
        else:
            print("Invalid choice! Try again.")


main()
