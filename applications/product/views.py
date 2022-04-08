from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from applications.product.filters import ProductFilter
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
    #permission_classes = [IsAuthenticatedOrReadOnly] # IsAdminUser
    # pagination_class = None
    pagination_class = LargeResultsSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price']
    #search_fields = ['name', 'description']
    # filterset_class = ProductFilter#
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(description__icontains=search))
        return queryset


class DeleteUpdateRetriveView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthor]   # [IsAdmin]




