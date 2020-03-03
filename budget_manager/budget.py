# Input a starting amount, the total amount you have available
available = 2500.00

# Create two empty dictionaries for budgets used and how much is expensed
budgets = {}
expenditure = {}

# Create a function that will name a budget type and reduce the budget from the total available
def add_budget(name, amount):
    global available

    # Make a function that will return an error if the same budget is used twice
    if name in budgets:
        raise ValueError("Budget Exists! Please choose another!")

    # Make another function that will return an error if the amount of the budget exceeds the available.
    if amount > available:
        raise ValueError("Insufficient Funds")

    budgets[name] = amount
    available -= amount
    expenditure[name] = 0
    return available
    
# Create a spending function that will track how much you've spent
def spend(name, amount):
    if name not in expenditure:
        raise ValueError("No Such Budget")
    expenditure[name] += amount

    # Track the amount left in the budget
    budgeted = budgets[name]
    spent = expenditure[name]
    return budgeted - spent

# Create a function that will print out a summary of your budget, expenses, and avaialble balance
def print_summary():
    # Create a format table to make the summary easier to read
    print("Budget              Budgeted   Spent Remaining")
    print("---------------------------------------------------------")

    # Create a "totals" variable for a footer section in the summary
    total_budgeted = 0
    total_spent = 0
    total_remaining = 0
    
    for name in budgets:
        budgeted = budgets[name]
        spent = expenditure[name]
        remaining = budgeted - spent

        # Start formatting the summary to be easier to read
        print(f'{name:15s} {budgeted:10.2f} {spent:10.2f} {remaining:10.2f}')

        # Add the amounts to the totals before this function
        total_budgeted += budgeted
        total_spent += spent
        total_remaining += remaining

    # Create the Footer
    print("---------------------------------------------------------")
    print(f'{"Total":15s} {total_budgeted:10.2f} {total_spent:10.2f} {total_budgeted - total_spent:10.2f}')
    

