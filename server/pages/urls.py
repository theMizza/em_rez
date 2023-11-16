from django.urls import path
from .views import index, about, contacts

urlpatterns = [
    path('', index, name='home_page'),
    path('about_us/', about, name='about_us'),
    path('contacts/', contacts, name='contacts')
]