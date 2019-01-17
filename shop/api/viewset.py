from rest_framework import viewsets, serializers
from rest_framework.response import Response

from shop.models import Category, Item
from .serializers import CategorySerializer, ItemSerializer
from rest_framework.views import APIView
from django.http import HttpResponse

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()