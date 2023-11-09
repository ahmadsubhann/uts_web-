from . import views
from django.urls import path


urlpatterns = [
    path('members/', views.members, name='members'),
    path('kategori/', views.kategori, name='kategori'),
]
