from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('signup', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename='login')
router.register('checkpoint', views.CheckpointViewSet, basename='checkpoint')
router.register('hunt', views.HuntViewSet, basename='hunt')
router.register('userhunt', views.UserHuntViewSet, basename='userhunt')
router.register('userimages', views.UserCheckpointImageViewSet, basename='usercheckpointimage')
urlpatterns = [
    url('', include(router.urls)),
]
