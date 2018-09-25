
from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    # post views
    path('', views.home, name='home'),
]