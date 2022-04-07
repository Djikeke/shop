from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from applications.product.models import Product
from applications.product.permissions import IsAdmin, IsAuthor
from applications.product.serializers import ProductSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 100


class ListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # IsAdminUser
    # pagination_class = None
    pagination_class = LargeResultsSetPagination


class DeleteUpdateRetriveView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthor]   # [IsAdmin]




