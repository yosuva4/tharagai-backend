
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('tharagai/products/',include("api.urls.product_url")),
    path('tharagai/users/',include("api.urls.user_url")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)