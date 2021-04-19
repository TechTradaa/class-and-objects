class Budget:

    balanced_list = list()
    balanced_list.append("food")
    balanced_list.append("entertainment")
    balanced_list.append("clothing")

    print(balanced_list)

    default_price = [0, 0, 0]

    def __init__(self, balanced_list, category_price):
        self.balanced_list = balanced_list
        self.category_price = category_price

    def deposit(self):
        balanced_list = list()
        default_price = [0, 0, 0]
        selected_balanced_list = input("which of these do you what to check? \n ")
        input_price = int(input("what is your Balance? /n"))
        old_price = default_price[balanced_list.index(selected_balanced_list)]
        if selected_balanced_list in balanced_list:
            old_price = default_price[balanced_list.index(selected_balanced_list)]
            category_price = old_price + input_price
            return old_price




