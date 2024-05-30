from django.urls import path
from api.views.user_views import AllProfiles,UserProfile,GetUser,UserRegistration,AddressViews
from rest_framework.authtoken import views

urlpatterns = [
    path("",AllProfiles.as_view()),
    path("<int:pk>/",UserProfile.as_view()),
    path("profile/",GetUser.as_view()),
    path("register/",UserRegistration.as_view()),
    path('login/', views.obtain_auth_token),
    
    path("address/",AddressViews.as_view()),

    # path("send-otp/",Send_otp.as_view()),
    # path("verify-otp/",Verify_otp.as_view()),
]