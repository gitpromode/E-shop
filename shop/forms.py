from django import forms
from .models import Category, Item, Unit, UnitConversion, Customer

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'parentId',)


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'available', 'brand', 'image',)


class UnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('label',)



class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'address', 'phone_number', 'location', 'active_inactive',)