# Input a starting amount, the total amount you have available
available = 2500.00

# Create two empty dictionaries for budgets used and how much is expensed
budgets = {}
expenditure = {}

# Create a function that will name a budget type and reduce the budget from the total available
def add_budget(name, amount):
    global available

    budgets[name] = amount
    available -= amount
    expenditure[name] = 0
    return available
    
