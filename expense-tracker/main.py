# Simple Expense Tracker

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = input("Enter expense amount: ")
        expenses.append(amount)
    elif choice == "2":
        print("Expenses:", expenses)
    elif choice == "3":
        break
    else:
        print("Invalid choice")
