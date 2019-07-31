from django.contrib import admin
from django.urls import path, include
import loginapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginapp.views.home, name="home"),
    path("accounts/", include("allauth.urls")),
]
