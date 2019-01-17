from django.shortcuts import render
from django.shortcuts import reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from .models import Category, Item
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm, ItemForm

# Create your views here.


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'shop/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('shop:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'shop/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('shop:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'shop/category_delete.html'
    success_url = reverse_lazy('shop:category_list')


class ItemListView(ListView):
    model = Item
    template_name = 'shop/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'shop/item_detail.html'


class ItemCreateView(CreateView):
    model = Item
    template_name = 'shop/item_form.html'
    form_class = ItemForm
    success_url = reverse_lazy('shop:item_list')


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'shop/item_form.html'
    form_class = ItemForm
    success_url = reverse_lazy('shop:item_list')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'shop/item_form.html'
    form_class = ItemForm
    success_url = reverse_lazy('shop:item_list')


class CategoryItemView(TemplateView):
    template_name = 'shop/category_item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs['category_pk'])
        context['category_item'] = Item.objects.filter(category_id=self.kwargs['category_pk'])
        return context
