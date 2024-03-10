from django.urls import path

from api.views import user_view

urlpatterns = [ 
    path('',user_view.getUsers),

    path('login/', user_view.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/',user_view.registerUser),
    path('profile/',user_view.getUserProfile),
]