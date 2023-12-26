from django.urls import path
from . import views 

urlpatterns = [
    path('HelloView/',views.helloapi.as_view()),
]
