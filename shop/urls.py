from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('category-list', views.CategoryListView.as_view(), name='category_list'),
    path('category-detail/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category-add', views.CategoryCreateView.as_view(), name='category_add'),
    path('category-edit/<int:pk>', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category-delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('item-list', views.ItemListView.as_view(), name='item_list'),
    path('item-detail/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('item-add', views.ItemCreateView.as_view(), name='item_add'),
    path('item-edit/<int:pk>', views.ItemUpdateView.as_view(), name='item_edit'),
    path('item-delete/<int:pk>', views.ItemDeleteView.as_view(), name='item_delete'),

    path('category-item/<int:category_pk>', views.CategoryItemView.as_view(), name="category_item"),
]