from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import APISignup, APIGetToken, UserViewSet

v1_router = DefaultRouter()
v1_router.register(
    'users',
    UserViewSet,
    basename='users'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token')
]
