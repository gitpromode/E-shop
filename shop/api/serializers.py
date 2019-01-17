from rest_framework import serializers

from shop.models import Category, Item

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'available', 'brand', 'created_at', 'updated_at', 'image', 'extra',)