class BudgetManager:
    def __init__(self, amount):
        # Input a starting amount, the total amount you have available
        self.available = amount

        # Create two empty dictionaries for budgets used and how much is expensed
        self.budgets = {}
        self.expenditure = {}

        # Create a function that will name a budget type and reduce the budget from the total available
        def add_budget(self, name, amount):

            # Make a function that will return an error if the same budget is used twice
            if name in self.budgets:
                raise ValueError("Budget Exists! Please choose another!")

            # Make another function that will return an error if the amount of the budget exceeds the available.
            if amount > self.available:
                raise ValueError("Insufficient Funds")

            self.budgets[name] = amount
            self.available -= amount
            self.expenditure[name] = 0
            return self.available
            
        # Create a spending function that will track how much you've spent
        def spend(self, name, amount):
            if name not in self.expenditure:
                raise ValueError("No Such Budget")
            self.expenditure[name] += amount

            # Track the amount left in the budget
            budgeted = self.budgets[name]
            spent = self.expenditure[name]
            return budgeted - spent

        # Create a function that will print out a summary of your budget, expenses, and avaialble balance
        def print_summary(self):
            # Create a format table to make the summary easier to read
            print("Budget              Budgeted   Spent Remaining")
            print("---------------------------------------------------------")

            # Create a "totals" variable for a footer section in the summary
            total_budgeted = 0
            total_spent = 0
            total_remaining = 0
            
            for name in self.budgets:
                budgeted = self.budgets[name]
                spent = self.expenditure[name]
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
            

