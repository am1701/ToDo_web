
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('lista.urls', namespace='lista'),),
    path("c/", include("accounts.urls", namespace="accounts"),),
    

]
