from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('HelloViewSet',views.helloviewset, basename = 'HelloViewSet')
router.register('Profile',views.ProfileViewset) 
router.register('feed',views.UserProfileFeedViewSet)


urlpatterns = [
    path('HelloView/',views.helloapi.as_view()),
    path('login/',views.UserLoginApiView.as_view()),    
    path('',include(router.urls)),
]
