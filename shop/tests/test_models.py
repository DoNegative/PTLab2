from django.test import TestCase
from shop.models import Product, Purchase, Promo
from datetime import datetime

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="table", price="740")
        Product.objects.create(name="pencil", price="50")

    def test_correctness_types(self):                   
        self.assertIsInstance(Product.objects.get(name="table").name, str)
        self.assertIsInstance(Product.objects.get(name="table").price, int)
        self.assertIsInstance(Product.objects.get(name="pencil").name, str)
        self.assertIsInstance(Product.objects.get(name="pencil").price, int)        

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="table").price == 740)
        self.assertTrue(Product.objects.get(name="pencil").price == 50)

class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_book = Product.objects.create(name="book", price="740")
        self.datetime = datetime.now()
        Purchase.objects.create(product=self.product_book,
                                person="Ivanov",
                                address="Svetlaya St.",
                                price="740"
                                )

    def test_correctness_types(self):
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).person, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).address, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).date, datetime)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).price, int)

    def test_correctness_data(self):
        self.assertTrue(Purchase.objects.get(product=self.product_book).person == "Ivanov")
        self.assertTrue(Purchase.objects.get(product=self.product_book).address == "Svetlaya St.")
        self.assertTrue(Purchase.objects.get(product=self.product_book).date.replace(microsecond=0) == \
            self.datetime.replace(microsecond=0))
        self.assertTrue(Purchase.objects.get(product=self.product_book).price == 740)

class Promo_test(TestCase):
    def setUp(self):
        Promo.objects.create(name="sale15", discount="15")

    def test_correctness_types(self):
        self.assertIsInstance(Promo.objects.get(name="sale15").name, str)
        self.assertIsInstance(Promo.objects.get(name="sale15").discount, int)

    def test_correctness_data(self):
        self.assertTrue(Promo.objects.get(name="sale15").discount == 15)
