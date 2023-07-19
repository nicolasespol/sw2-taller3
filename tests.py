import unittest

from main import DiningExperienceManager


class TestDiningExperienceManager(unittest.TestCase):
    def setUp(self):
        self.manager = DiningExperienceManager()
        self.manager.order = {}  # Clear the previous orders

    def test_select_meal(self):
        # Test selecting a valid meal
        self.assertEqual(self.manager.select_meal("Chinese", "Kung Pao Chicken", 2), "Meal added to order successfully.")

        # Test selecting a meal with invalid category
        self.assertEqual(self.manager.select_meal("Indian", "Kung Pao Chicken", 2), "Error: Indian is not available on the menu.")

        # Test selecting a meal that is not in the category
        self.assertEqual(self.manager.select_meal("Chinese", "Pizza Margherita", 2), "Error: Pizza Margherita is not available in the Chinese category.")

        # Test selecting a meal with quantity <= 0
        self.assertEqual(self.manager.select_meal("Chinese", "Kung Pao Chicken", 0), "Error: Quantity should be a positive integer greater than zero and less than or equal to 100.")

        # Test selecting a meal with quantity > 100
        self.assertEqual(self.manager.select_meal("Chinese", "Kung Pao Chicken", 101), "Error: Quantity should be a positive integer greater than zero and less than or equal to 100.")

    def test_calculate_cost(self):
        # Test cost calculation for one meal
        self.manager.select_meal("Chinese", "Kung Pao Chicken", 2)
        self.assertEqual(self.manager.calculate_cost(), 10)

        # Clear the previous orders
        self.manager.order = {}

        # Test cost calculation for multiple meals
        self.manager.select_meal("Italian", "Lasagna", 3)
        self.assertEqual(self.manager.calculate_cost(), 15)

        # Clear the previous orders
        self.manager.order = {}

        # Test cost calculation with quantity discount
        self.manager.select_meal("Pastries", "Croissant", 3)
        self.manager.select_meal("Chinese", "Kung Pao Chicken", 2)
        self.manager.select_meal("Italian", "Lasagna", 1)
        self.assertEqual(self.manager.calculate_cost(), 27)  # With 10% discount

        # Clear the previous orders
        self.manager.order = {}

        # Test cost calculation with total cost discount
        self.manager.select_meal("Pastries", "Pain au Chocolat", 11)
        self.assertEqual(self.manager.calculate_cost(), 44)  # With 20% discount and $10 discount

        # Clear the previous orders
        self.manager.order = {}

        # Test cost calculation with Chef's Specials surcharge
        self.manager.select_meal("Chef's Specials", "Caviar", 1)
        self.assertEqual(self.manager.calculate_cost(), 21)  # With 5% surcharge

    def test_finalize_order(self):
        # Test finalizing order
        self.manager.select_meal("Chinese", "Kung Pao Chicken", 2)
        self.manager.select_meal("Italian", "Lasagna", 3)
        self.manager.select_meal("Pastries", "Croissant", 3)
        self.manager.select_meal("Pastries", "Pain au Chocolat", 6)
        self.manager.select_meal("Chef's Specials", "Caviar", 1)
        order, cost = self.manager.finalize_order()
        self.assertEqual(order, {("Chinese", "Kung Pao Chicken"): 2, ("Italian", "Lasagna"): 3, ("Pastries", "Croissant"): 3, ("Pastries", "Pain au Chocolat"): 6, ("Chef's Specials", "Caviar"): 1})
        self.assertEqual(cost, 63)  # With 20% discount, $25 discount, and 5% surcharge


if __name__ == "__main__":
    unittest.main()
