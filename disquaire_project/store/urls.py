from django.urls import path

from . import views

urlpatterns = [
    path('', views.listing, name='listing'),  # "/store" will call the method "index" in "views.py"
    path('<int:album_id>', views.detail, name='detail'),
    path('search/', views.search, name='search')
]
