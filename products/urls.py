from django.urls import path
from . import views

# the root url is mapped to the view function
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]