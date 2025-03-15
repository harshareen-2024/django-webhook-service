from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WebhookViewSet, LoginAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)  # ✅ Import TokenRefreshView
from .views import DestinationViewSet

from .views import (
    AccountViewSet,
    DestinationViewSet,
    AccountMemberViewSet,
    WebhookViewSet,
)

router = DefaultRouter()
router.register(r"webhooks", WebhookViewSet)
router.register(r"accounts", AccountViewSet)
router.register(r"destinations", DestinationViewSet)
router.register(r"account-members", AccountMemberViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api/login/", LoginAPIView.as_view(), name="login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
