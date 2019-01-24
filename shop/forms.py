from django import forms
from .models import Category, Item

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'parentId',)


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'available', 'brand', 'image',)