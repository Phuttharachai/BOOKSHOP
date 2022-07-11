from django.urls import path, include
from rest_framework.routers import DefaultRouter
from book import views
from book.models import Type, Writer, Customer, Order, Book

router = DefaultRouter()
router.register(r'types', views.TypeViewSet)
router.register(r'writers', views.WriterViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'books', views.BookViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
