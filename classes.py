class Bikes():

    def __init__(self,description, cost, sale_price, condition, sold):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
        self.sold = sold

    def update_sale_price(self, sale_price):
        if self.sold:
            return 'Action not allowed, Bike has already been sold'
        else:
            self.sale_price = sale_price
            return f"{self} sale price has been updated to {self.sale_price}"

    def sell(self):
        self.sold = True


bike1 = Bikes('Mountain', 1900, 2200, 'new', False)
bike2 = Bikes('Road', 5000, 8000, 'new', False)
bike3 = Bikes('Hybard', 1000, 1500, 'new', False)

print(bike3.sale_price)
print(bike3.sell())
print(bike3.update_sale_price(23000))

print(bike1.sale_price)
# print(bike1.sell())
# bike1.update_sale_price(9000)
print(bike1.update_sale_price(9000))
print(bike1.sale_price)
