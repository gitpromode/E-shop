from rest_framework import viewsets, serializers
from rest_framework.response import Response

from shop.models import Category, Item, Unit, UnitConversion, Customer, Sale, Row
from .serializers import CategorySerializer, ItemSerializer, UnitSerializer, UnitConversionSerializer, CustomerSerializer, \
    SaleSerializer, RowSerializer
from rest_framework.views import APIView
from django.http import HttpResponse

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class UnitViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()


class UnitConversionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UnitConversionSerializer
    queryset = UnitConversion.objects.all()


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class SaleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


class RowViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RowSerializer
    queryset = Row.objects.all()