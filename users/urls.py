from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import EmailConfirmationView, UserViewSet


router = DefaultRouter()
router.register(r'auth', EmailConfirmationView, 'email_confirm')
router.register(r'users', UserViewSet, 'admin_users')


urlpatterns = [
    path('v1/auth/', include(router.urls)),
    path('v1/', include(router.urls)),
]
