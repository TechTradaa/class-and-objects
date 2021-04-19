class Budget:

    balanced_list = list()
    balanced_list.append("food")
    balanced_list.append("entertainment")
    balanced_list.append("clothing")

    print(balanced_list)

    default_price = [0, 0, 0]

    selected_balanced_list = input("which of these do you what to check? \n ")
    input_price = int(input("what is your Balance? /n"))
    old_price = default_price[balanced_list.index(selected_balanced_list)]
    category_price = old_price + input_price

    def __init__(self, category_price):
        self.category_price = category_price

    def deposit(self):
        if selected_balanced_list in balanced_list:
            old_price = default_price[balanced_list.index(selected_balanced_list)]
            print()

    def withdraw(self):
        if selected_balanced_list in balanced_list:
            old_price = default_price[balanced_list.index(selected_balanced_list)]
            print()

    def balance(self):
        if selected_balanced_list in balanced_list:
            old_price = default_price[balanced_list.index(selected_balanced_list)]
            print()

    def transfer(self):
        if selected_balanced_list in balanced_list:
            old_price = default_price[balanced_list.index(selected_balanced_list)]
            print()


food_category = Budget(diff_category_price)
clothing_category = Budget(diff_category_price)
data_category = Budget(diff_category_price)








