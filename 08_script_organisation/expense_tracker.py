"""A small command-line expense tracker."""


def add_expense(expenses, description, amount):
    """Add one expense (a dictionary) to the list."""
    expenses.append({"description": description, "amount": amount})


def total_expenses(expenses):
    """Return the sum of all expense amounts."""
    return sum(item["amount"] for item in expenses)


def show_summary(expenses):
    """Print every expense and the total."""
    if not expenses:
        print("No expenses recorded.")
        return
    for number, item in enumerate(expenses, start=1):
        print(f"{number}. {item['description']}: {item['amount']:.2f}")
    print(f"Total: {total_expenses(expenses):.2f}")


def main():
    """Run the menu loop."""
    expenses = []
    while True:
        choice = input("Choose: (a)dd, (s)ummary, (q)uit: ").lower()
        if choice == "a":
            description = input("Description: ")
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Amount must be a number.")
                continue
            add_expense(expenses, description, amount)
        elif choice == "s":
            show_summary(expenses)
        elif choice == "q":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
