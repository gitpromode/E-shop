from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import Category, Item
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm, ItemForm

# Create your views here.


class CategoryListView(ListView):
    """
        Category List View
    """
    model = Category
    template_name = 'shop/category_list.html'


class CategoryDetailView(DetailView):
    """
        Category Detail View
    """
    model = Category
    template_name = 'shop/category_detail.html'


class CategoryCreateView(CreateView):
    """
        Category Create View
    """
    model = Category
    template_name = 'shop/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('shop:category_list')


class CategoryUpdateView(UpdateView):
    """
        Category Update View
    """
    model = Category
    template_name = 'shop/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('shop:category_list')


class CategoryDeleteView(DeleteView):
    """
        Category Delete View
    """
    model = Category
    template_name = 'shop/category_delete.html'
    success_url = reverse_lazy('shop:category_list')


class CategoryItemView(TemplateView):
    """
        Category-Item Template View
    """
    template_name = 'shop/category_item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs['category_pk'])
        context['category_item'] = Item.objects.filter(category_id=self.kwargs['category_pk'])
        return context


class ItemDetailView(DetailView):
    """
        Item Detail View
    """
    model = Item
    template_name = 'shop/item_detail.html'


class ItemCreateView(CreateView):
    """
        Item Create View
    """
    model = Item
    template_name = 'shop/item_form.html'
    form_class = ItemForm

    def form_valid(self, form):
        form.instance.category = get_object_or_404(Category, pk=self.kwargs['category_pk'])
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_pk'])
        return context

    def get_success_url(self):
            success_url = reverse_lazy('shop:category_item', args=(self.kwargs['category_pk'],))
            return success_url


class ItemUpdateView(UpdateView):
    """
        Item Update View
    """
    model = Item
    template_name = 'shop/item_form.html'
    form_class = ItemForm

    def get_success_url(self):
            success_url = reverse_lazy('shop:category_item', args=(self.object.category.pk,))
            return success_url


class ItemDeleteView(DeleteView):
    """
        Item Delete View
    """
    model = Item
    template_name = 'shop/item_delete.html'
    form_class = ItemForm

    def get_success_url(self):
            success_url = reverse_lazy('shop:category_item', args=(self.object.category.pk,))
            return success_url



