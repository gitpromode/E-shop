from django.urls import path, include
from rest_framework import routers

from . import viewset

router = routers.DefaultRouter()

urlpatterns = [
	path('', include(router.urls)),
    path('category/', viewset.CategoryViewSet.as_view({'get': 'list'})),
    path('item/', viewset.ItemViewSet.as_view({'get': 'list'})),
    path('unit/', viewset.UnitViewSet.as_view({'get': 'list'})),
    path('unitconversion/', viewset.UnitConversionViewSet.as_view({'get': 'list'})),
    path('customer/', viewset.CustomerViewSet.as_view({'get': 'list'})),
    path('sale/', viewset.SaleViewSet.as_view({'get': 'list'})),
    path('row/', viewset.RowViewSet.as_view({'get': 'list'})),
]