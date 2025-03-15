from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


# Redirect root URL to Swagger docs
def redirect_to_docs(request):
    return redirect("/docs/")


# API Documentation setup
schema_view = get_schema_view(
    openapi.Info(
        title="Webhook API",
        default_version="v1",
        description="API for Webhook Service",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirect_to_docs),  # Redirect root URL to API docs
    path("api/", include("webhook.urls")),  # Your API endpoints
    # Swagger UI and ReDoc
    re_path(
        r"^docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
