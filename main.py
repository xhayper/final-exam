class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(self, item):
        return DeliveryOrder(self, item)

class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self, order):
        print(f"{self.name} is delivering {order.item} to {order.customer.name} using {self.vehicle}.")
        order.status = "delivered"

class DeliveryOrder:
    def __init__(self, customer, item):
        self.customer = customer
        self.item = item
        self.status = "preparing"

    def assign_driver(self, driver):
        self.driver = driver

    def summary(self):
        return "Order Summary:\n" + \
            f"Item: {self.item}\n" + \
            f"Customer: {self.customer.name}\n" + \
            f"Status: {self.status}\n" + \
            f"Driver: {self.driver.name}"

def main():
    alice = Customer("Alice", "Thailand")
    bob = Customer("Bob", "USA")
    david = Driver("David", "motorcycle")

    alice.introduce()
    bob.introduce()
    david.introduce()

    print()

    laptop_order = alice.place_order("Laptop")
    laptop_order.assign_driver(david)
    headphones_order = bob.place_order("Headphones")
    headphones_order.assign_driver(david)

    print(laptop_order.summary())
    print()
    print(headphones_order.summary())

    print()

    david.deliver(laptop_order)
    david.deliver(headphones_order)

    print()

    print("Final Status:")
    print(f"Order for Laptop → {laptop_order.status}")
    print(f"Order for Headphones → {headphones_order.status}")


if __name__ == "__main__":
    main()