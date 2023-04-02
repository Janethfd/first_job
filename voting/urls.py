
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boss.urls')),
    path('', include("users.urls")),
    path("", include('django.contrib.auth.urls')),

]