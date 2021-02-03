from profiles_api import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile',views.UserProfileViewSets,base_name='')
urlpatterns = [
    path('test-views/',views.TestApiView.as_view()),
    path('',include(router.urls))
]
