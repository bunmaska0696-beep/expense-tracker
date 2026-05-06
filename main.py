import json

def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def add_expense():
    name = input("What did you buy? ")
    amount = float(input("How much did it cost? "))

    data = load_data()

    new_expense = {
        "name": name,
        "amount": amount
    }

    data.append(new_expense)
    save_data(data)

    print("Saved!")

def view_expenses():
    data = load_data()

    print("\nYour Expenses:")
    for expense in data:
        print(f"{expense['name']} - £{expense['amount']:.2f}")

def total_expenses():
    data = load_data()

    total = 0
    for expense in data:
        total = total + expense["amount"]

    print(f"Total spent: £{total:.2f}")

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")