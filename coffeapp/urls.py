from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from coffeapp.views import FrontendAppView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    # Authentication (Djoser + JWT)
    path('auth/', include('djoser.urls')),          # /auth/users/, /auth/users/me/
    path('auth/', include('djoser.urls.jwt')),      # /auth/jwt/create/, etc.
    
    path("api/inventory/", include("apps.inventory.urls")),
    path("api/orders/", include("apps.orders.urls")),
    path("api/payments/", include("apps.payments.urls")),
    path("api/products/", include("apps.products.urls")),
    re_path(r'^.*$', FrontendAppView.as_view(), name='home'),

] 
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
