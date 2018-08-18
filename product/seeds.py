from .models import *
from random import *
from decimal import Decimal


class Seeder:

    def __init__(self):
        self.products = ["Orange Ball", "Chew Toy 1", "Cat Bowl", "Dog Bed", "Cat Food", "Dog Food"]

    def seed(self):
        for x in range(20):
            title = choice(self.products) + " {0}".format(randint(1, 10000))
            price = float(format(Decimal(str(random())), '.2f'))
            quantity = randint(1, 100)
            customer = User.objects.get(pk=randint(1,3))
            product = Products(title=title, price=price)
            product.save()
            sale = Sales(product=product, quantity=quantity, customer=customer)
            sale.save()
