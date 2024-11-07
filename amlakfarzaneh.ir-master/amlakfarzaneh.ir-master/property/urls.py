from django.urls import path

from property.views import EstateListView

urlpatterns = [

    path('category/<str:url_slug>', EstateListView.as_view(), name='Estate_by_category_list'),

]
