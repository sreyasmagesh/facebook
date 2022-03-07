from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index2),
    path('new',views.index),
    path('fb',views.index3),
    path('artofsoul',views.index4)
]
