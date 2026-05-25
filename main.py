class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_stock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"{self.name} (ID: {self.product_id}) stock: {self.quantity} (+{amount})")
        elif amount < 0:
            if (self.quantity - amount) >= 0:
                self.quantity += amount
                print(f"{self.name} (ID: {self.product_id}) stock: {self.quantity} ({amount})")
        else:
            print("Invalid amount")
            print(f"{self.name} ({self.product_id}) stock: {self.quantity} ({amount})")

    def get_total_value(self):
        totalValue = self.quantity * self.price

        return totalValue

    def __str__(self):
        # TODO: Format output nicely
        return ""

class Inventory:
    def __init__(self):
        self.products = {} # Maps product_id -> Product object

    def add_product(self, product):
        # TODO: Add to dictionary
        pass

    def display_all(self):
        # TODO: Iterate and print
        pass

Apple = Product("9123413", "Apple", 0.5, 312)

if __name__ == "__main__": # research what __main__ and __name__ actually does!
    # TODO: Write a while loop to interact with user 
    print("Welcome to the Inventory Manager")