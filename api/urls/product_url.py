from django.urls import path
from api.views.product_views import BestSeller, Products,ProductGet,ProductAdd,CartView,FilterProduct,ProductTypeView

urlpatterns = [
    path('',Products.as_view()),
    path("bestSeller/",BestSeller.as_view()),
    path("categories/",ProductTypeView.as_view()),
    # path("all-products/",Products.as_view()),
    # path("product-filter/<str:pk>/",FilterProduct.as_view()),
    # path("product-get/<int:pk>/",ProductGet.as_view()),
    # path("add-product/",ProductAdd.as_view()),
    # path("cart/",CartView.as_view()),
    # path("cart/<int:id>/",CartView.as_view()),
]   