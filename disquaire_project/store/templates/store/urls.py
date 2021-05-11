from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('store/', include('store.urls')),
    path('admin/', admin.site.urls)
]
