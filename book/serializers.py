from rest_framework import serializers
from book.models import Type, Writer, Customer, Order, Book

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    def validate_book(self, value):

        book_ids = [book.id for book in value]
        sold_book = Book.objects.filter(pk__in=book_ids, order__isnull=False)
        if sold_book:
            raise serializers.ValidationError(
                'one or more of the provided books were already sold.')
        return value

    class Meta:
        model = Order
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


