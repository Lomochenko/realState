from django.urls import path
from . import views
from .views import add_phone_number,location,allProperty,property

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('advertising/', add_phone_number, name='add_phone_number'),
    path('location/', location, name='location'),
    path('allProperty/', allProperty, name='allProperty'),
    path('property/', property, name='property'),
]
