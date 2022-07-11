from rest_framework import permissions, viewsets, mixins, status
from book.models import Type, Writer, Customer, Order, Book
from book.serializers import TypeSerializer, WriterSerializer, CustomerSerializer, OrderSerializer, BookSerializer
from rest_framework.response import Response


class TypeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwarg):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        type = Type.objects.get(pk=kwargs['pk'])
        serializer = CustomerSerializer(type)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WriterViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwarg):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        writer = Writer.objects.get(pk=kwargs['pk'])
        serializer = WriterSerializer(writer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        customer = Customer.objects.get(pk=kwargs['pk'])
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs['pk'])
        serializer = CustomerSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        serializer = CustomerSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
