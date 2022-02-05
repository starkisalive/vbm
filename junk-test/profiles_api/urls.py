from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profiles', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('home/', views.HomeView),
    path('', include(router.urls))
]
