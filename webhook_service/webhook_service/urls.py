"""
URL configuration for webhook_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("webhook.urls")),
]


def redirect_to_docs(request):
    return redirect("/docs/")  # Redirect root URL to API documentation


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirect_to_docs),  # Redirect root URL to API docs
    path("api/", include("webhook.urls")),  # Your API endpoints
    # path("docs/", include("drf_yasg.urls")),  # Swagger documentation
]


schema_view = get_schema_view(
    openapi.Info(
        title="Webhook API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", redirect_to_docs),
    path("", include("home.urls")),
]
