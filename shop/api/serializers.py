from rest_framework import serializers

from shop.models import Category, Item, Unit, UnitConversion, Customer, Sale, Row

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'parentId',)


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'available', 'brand', 'created_at', 'updated_at', 'image', 'extra',)


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ('label',)


class UnitConversionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnitConversion
        fields = ('from_unit', 'to_unit', 'number_of_multiples',)


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('name', 'address', 'customer', 'phone_number', 'location', 'active_inactive',)


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('bill_number', 'date', 'customer', 'receive_amount', 'return_amount', 'due_amount', 'total_amount',)


class RowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Row
        fields = ('sale', 'item', 'quantity', 'unit', 'discount',)





