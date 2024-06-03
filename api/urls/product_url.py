from django.urls import path
from api.views.product_views import add_product,BestSeller, Products,ProductGet,ProductAdd,CartView,FilterProduct,ProductTypeView

urlpatterns = [
    path('product/',Products.as_view()),
    path('add-product/',add_product),
    # path("bestSeller/",BestSeller.as_view()),
    # path("all-products/",Products.as_view()),
    # path("product-type/",ProductTypeView.as_view()),
    # path("product-filter/<str:pk>/",FilterProduct.as_view()),
    # path("product-get/<int:pk>/",ProductGet.as_view()),
    # path("add-product/",ProductAdd.as_view()),
    # path("cart/",CartView.as_view()),
    # path("cart/<int:id>/",CartView.as_view()),
]