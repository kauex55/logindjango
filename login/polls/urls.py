from django.urls import path

from polls.views import index,ola

urlpatterns = [
    path('index/', index, name="index" ),
    path('ola/', ola, name="ola"),
]