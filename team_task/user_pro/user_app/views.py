from rest_framework import generics
from .models import Product, Feedback
from .serializers import ProductSerializer, FeedbackSerializer
from rest_framework.filters import OrderingFilter,SearchFilter

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('product_name','price','category')
    ordering_fields=('product_name','price','id')


class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

