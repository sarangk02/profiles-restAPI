from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('HelloViewSet',views.helloviewset, basename = 'HelloViewSet')

urlpatterns = [
    path('HelloView/',views.helloapi.as_view()),
    path('',include(router.urls))
]
