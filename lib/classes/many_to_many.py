class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

        self._orders = []
        self._customers = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and len(name) >= 3:
            self._name = name
        else: 
            print("Name must be a string greater than or equal to three characters and cannot be reset.")
        
    def orders(self):
        return self._orders
    
    def customers(self):
        return list(set(self._customers))
    
    def num_orders(self):
       return len(self._orders)
    
    def average_price(self):
        if self.num_orders() == 0: 
            return 0
        else:
            import statistics
            return statistics.mean([o.price for o in self._orders])


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

        self._orders = []
        self._coffees = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            print("Name must be a string between 1 and 15 characters and cannot be changed")
        
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(self._coffees))
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        [c._orders.append(new_order) for c in Coffee.all if c.name == coffee]
        return new_order
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

        coffee._orders.append(self)
        coffee._customers.append(customer)

        customer._orders.append(self)
        customer._coffees.append(coffee)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            print("Customer must be an instance of Customer")

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            print("Coffee must be an instance of Coffee")

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if type(price) is float and 1.0 <= price <= 10.0 and not hasattr(self, "price"):
            self._price = price
        else:
            print("Cannot reset price")