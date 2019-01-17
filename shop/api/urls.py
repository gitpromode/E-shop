from django.urls import path, include
from rest_framework import routers

from . import viewset

router = routers.DefaultRouter()

urlpatterns = [
	path('', include(router.urls)),
    path('category/', viewset.CategoryViewSet.as_view({'get': 'list'})),
    path('item/', viewset.ItemViewSet.as_view({'get': 'list'})),
]