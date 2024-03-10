
from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('',views.getRoutes,name='routes'),

    path('users/',views.getUsers),
    path('users/register/',views.registerUser),
    path('users/profile/',views.getUserProfile),
    
    path('products/',views.getProducts),
    path('product/<str:pk>/',views.getProduct),
    
]
