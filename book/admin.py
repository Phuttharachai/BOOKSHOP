from django.contrib import admin
from book.models import Type, Writer, Customer, Order, Book


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
