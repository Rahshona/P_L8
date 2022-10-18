class StoreOfTech():
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.result = {'Name': self.name, 'Price': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} - price: {self.price}, quantity: {self.quantity}'

    def reception(self):
        try:
            my = input('Write the name')
            my_p = input('Write the price')
            my_q = input('Write the quantity')
            unique = {'Name': my, 'Price': my_p, 'Quantity': my_q}
            self.result.update(unique)
            self.my_store.append(self.result)
            print(f'Full list: \n {self.my_store}')
        except:
            return 'Err. Try again'

        print(f'For exiting - Q, continuing - Enter')
        q = input('')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Full store -\n {self.my_store_full}')
            return f'Exit'
        else:
            return StoreOfTech.reception(self)


class Printer(StoreOfTech):
    def to_print(self):
        return 'to print'


class Scanner(StoreOfTech):
    def to_scan(self):
        return 'to scan'


class Copier(StoreOfTech):
    def to_copier(self):
        return 'to copy'


u_1 = Printer('aa', 12, 3)
u_2 = Scanner('aaa', 11, 9)
u_3 = Copier('aaaa', 1, 1)
print(u_1.reception())
print(u_2.reception())
print(u_3.reception())
print(u_1.to_print())
print(u_2.to_scan())
print(u_3.to_copier())

