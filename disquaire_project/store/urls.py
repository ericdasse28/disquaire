from django.urls import path

from . import views

urlpatterns = [
    path('', views.listing),  # "/store" will call the method "index" in "views.py"
    path('<int:album_id>', views.detail),
    path('search/', views.search)
]
