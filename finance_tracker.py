# Function to add a new expense to the data
def add_expense(data):
    # Get a valid expense description from the user
    while True:
        try:
            description = input("\nEnter expense description: ")
            if not description:
                raise ValueError
            break
        except ValueError:
            print("Please enter a description.")
                
    # Get a valid category from the user
    while True:
        try:
            category = input("Enter category: ")
            if not category:
                raise ValueError
            break
        except ValueError:
            print("Please enter a category.\n")

    # Get a valid amount from the user
    while True:
        try:
            amount = float(input("Enter amount: "))
            if not amount or amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid amount! Please enter a valid number.\n")

    # Add the expense to the correct category
    if category not in data:
        data[category] = []
    data[category].append((description, amount))
    return

# Function to display all recorded expenses
def view_expenses(data):
    if not data:
        print("\nThere are no expenses to view.\n")
        return

    print("\nAll Expenses:")
    for category, expenses in data.items():
        print(f"Category: {category}")
        for description, amount in expenses:
            print(f"  - {description}: ${amount}\n")
    return

# Function to display a summary (total amount) per category
def view_summary(data):
    if not data:
        print("\nThere are no expenses to summarize.\n")
    else:
        print("\nSummary:")
        for category, expenses in data.items():
            total = sum(amount for _, amount in expenses)
            print(f"{category}: ${total}\n")
    return

# Main function to run the finance tracker
def main():
    data = {}  # Dictionary to store expenses

    while True:
        print("Welcome to the Personal Finance Tracker")
        try:
            # Prompt the user to choose an action
            choice = int(input("What would you like to do?\n" +
              "1. Add Expense\n2. View All Expenses\n3. View Summary\n4. Exit\nChoose an option: "))
            
            # Ensure the user's choice is valid
            while choice < 1 or choice > 4:
                choice = int(input("\nPlease select a number between 1 and 4, inclusive.\n" +
                    "1. Add Expense\n2. View All Expenses\n3. View Summary\n4. Exit\nChoose an option: "))

        except ValueError:
            print("\nInvalid input! Please enter a valid number.\n")

        else:
            # Perform the chosen action
            if choice == 1:
                add_expense(data)
                print("\nExpense added successfully.\n")
            
            elif choice == 2:
                view_expenses(data)

            elif choice == 3:
                view_summary(data)

            elif choice == 4:
                print("\nHave a great day! Goodbye.\n")
                break

# Run the program
main()