from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Writer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField("Full name", max_length=1024)
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024)
    postal_code = models.CharField("ZIP / Postal code", max_length=12)
    city = models.CharField("City", max_length=1024)
    country = models.CharField("Country", max_length=100)
    phone = models.CharField(max_length=14)
    mailaddress = models.CharField(max_length=100)
    birthdate = models.DateField()


class Book(models.Model):
    currencies = [
        ('฿', "THB (฿)"),
    ]
    name = models.CharField(max_length=200)
    writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, choices=currencies, default="฿")
    description = models.TextField()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL, blank=True)
    date = models.DateField()
