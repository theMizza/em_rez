from django.urls import path
from .views import index, static_page_handler

urlpatterns = [
    path('', index, name='home_page'),
    path('<str:slug>/', static_page_handler)
]