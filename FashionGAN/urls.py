from django.urls import path
from django.urls import include
from . import views
urlpatterns=[
    path("",views.home),
    path("tryon/<int:id>",views.try_clothes_on,name='item_detail'),
    ]