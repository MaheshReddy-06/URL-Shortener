from django.contrib import admin
from django.urls import path

from .views import Urlgenerate, redirect_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Urlgenerate.as_view(), name='home'),
    path('s/<str:alias>/', redirect_url, name='redirect_url'),
]