from django.urls import path

from . import views

app_name = 'Initial_Terror'
urlpatterns = [
    path('', views.home, name='home'),
]