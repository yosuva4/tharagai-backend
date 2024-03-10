
from django.urls import path

from api.views import product_view

urlpatterns = [

    path('',product_view.getProducts),
    path('<str:pk>/',product_view.getProduct),
    
]
