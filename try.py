class Budget:
    balanced_list = list()
    balanced_list.append("food")
    balanced_list.append("entertainment")
    balanced_list.append("clothing")

    def __init__(self, amount):
        self.category = ["food", "entertainment", "clothing"]
        self.amount = amount

    def deposit(self):
        balanced_list = ["food", "entertainment", "clothing"]
        default_price = [0, 0, 0]
        selected_balanced_list = input("Select a Category? \n ")
        input_price = int(input("Deposit Amount? \n"))
        amount = default_price[balanced_list.index(selected_balanced_list)] + input_price
        return amount

    def withdraw(self):
        balanced_list = ["food", "entertainment", "clothing"]
        default_price = [0, 0, 0]
        selected_balanced_list = input("Select a Category? \n ")
        input_price = int(input("Withdrawal Amount? \n"))
        amount = default_price[balanced_list.index(selected_balanced_list)] + input_price
        return amount

    def check_balance(self):
        balanced_list = ["food", "entertainment", "clothing"]
        default_price = [0, 0, 0]
        selected_balanced_list = input("Select a Category? \n ")
        amount = default_price[balanced_list.index(selected_balanced_list)]

    def transfer(self, amount, other_instances):
        balanced_list = ["food", "entertainment", "clothing"]
        default_price = [0, 0, 0]
        selected_balanced_list = input("Select a Category? \n ")
        input_price = int(input("Deposit Amount? \n"))
        amount = default_price[balanced_list.index(selected_balanced_list)] + input_price
        if self.check_balance >= amount:
            other_instances.balance += amount
            self.check_balance -= amount
        else:
            print("checking balance Unsuccessful")


food_budget = Budget("food")
entertainment_budget = Budget("entertainment")
clothing_budget = Budget("clothing")

print(food_budget.deposit())
print(food_budget.withdraw())
print(food_budget.check_balance())
print(food_budget.transfer())
print(entertainment_budget.deposit())
print(entertainment_budget.withdraw())
print(entertainment_budget.check_balance())
print(entertainment_budget.transfer())
print(clothing_budget.deposit())
print(clothing_budget.withdraw())
print(clothing_budget.check_balance())
print(clothing_budget.transfer())