from django.urls import path
from . import views
from .views import add_phone_number

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('advertising/', add_phone_number, name='add_phone_number'),
]
