class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1, 16):
            self._name = name
        else:
            raise Exception

    def orders(self, new_order=None):
        from classes.order import Order

        return [o for o in Order.all if o.customer == self]

    def coffees(self):
        return list(set([o.coffee for o in self.orders()]))
