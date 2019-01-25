from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('category-list', views.CategoryListView.as_view(), name='category_list'),
    path('category-detail/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category-add', views.CategoryCreateView.as_view(), name='category_add'),
    path('category-edit/<int:pk>', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category-delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('category-item/<int:category_pk>', views.CategoryItemView.as_view(), name="category_item"),
    path('item-detail/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('item-add/<int:category_pk>', views.ItemCreateView.as_view(), name='item_add'),
    path('item-edit/<int:pk>', views.ItemUpdateView.as_view(), name='item_edit'),
    path('item-delete/<int:pk>', views.ItemDeleteView.as_view(), name='item_delete'),

    path('unit-list', views.UnitListView.as_view(), name='unit_list'),
    path('unit-detail/<int:pk>', views.UnitDetailView.as_view(), name='unit_detail'),
    path('unit-add', views.UnitCreateView.as_view(), name='unit_add'),
    path('unit-edit/<int:pk>', views.UnitUpdateView.as_view(), name='unit_edit'),
    path('unit-delete/<int:pk>', views.UnitDeleteView.as_view(), name='unit_delete'),

    path('customer-list', views.CustomerListView.as_view(), name='customer_list'),
    path('customer-detail/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('customer-add', views.CustomerCreateView.as_view(), name='customer_add'),
    path('customer-edit/<int:pk>', views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('customer-delete/<int:pk>', views.CustomerDeleteView.as_view(), name='customer_delete'),
]