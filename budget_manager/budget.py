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
    
