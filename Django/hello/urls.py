from django.urls import path
from . import views

urlpatterns = [
    path("bio/", views.home,name='home'),
]