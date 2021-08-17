from apps.views import hello
from django.urls import path
from .views import hello,route_Url

urlpatterns = [
    path('',hello),
    path('<slug:key>',route_Url)
]