# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class DiningExperienceManager:
    MENU = {
        "Chinese": {"Kung Pao Chicken": 5, "Sweet and Sour Pork": 5, "Fried Rice": 5},
        "Italian": {"Spaghetti Bolognese": 5, "Pizza Margherita": 5, "Lasagna": 5},
        "Pastries": {"Croissant": 5, "Baguette": 5, "Pain au Chocolat": 5},
        "Chef's Specials": {"Lobster Thermidor": 15, "Caviar": 20, "Truffle Pasta": 10},
    }

    def __init__(self):
        self.order = {}

    def select_meal(self, category, meal, quantity):
        if category not in self.MENU:
            return f"Error: {category} is not available on the menu."
        if meal not in self.MENU[category]:
            return f"Error: {meal} is not available in the {category} category."
        if quantity <= 0 or quantity > 100:
            return "Error: Quantity should be a positive integer greater than zero and less than or equal to 100."
        self.order[(category, meal)] = quantity
        return "Meal added to order successfully."

    def calculate_cost(self):
        total_cost = 0
        total_quantity = 0
        for (category, meal), quantity in self.order.items():
            total_cost += self.MENU[category][meal] * quantity
            total_quantity += quantity
        if total_quantity > 10:
            total_cost *= 0.8
        elif total_quantity > 5:
            total_cost *= 0.9
        if total_cost > 100:
            total_cost -= 25
        elif total_cost > 50:
            total_cost -= 10
        for (category, meal), quantity in self.order.items():
            if category == "Chef's Specials":
                total_cost += self.MENU[category][meal] * quantity * 0.05
        return total_cost

    def finalize_order(self):
        return self.order, self.calculate_cost()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    manager = DiningExperienceManager()
    print(manager.select_meal("Chinese", "Kung Pao Chicken", 2))
    print(manager.select_meal("Italian", "Lasagna", 3))
    print(manager.select_meal("Chef's Specials", "Caviar", 1))
    order, cost = manager.finalize_order()
    print("Order:", order)
    print("Total Cost:", cost)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
