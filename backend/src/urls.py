from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.urls import include, path
from django.shortcuts import redirect

# from ...views import ...ViewSet

router = DefaultRouter()
# router.register(r"", ...ViewSet)
 

@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "auth_register": reverse("register", request=request, format=format),
            "auth_login": reverse("login", request=request, format=format),
            "auth_logout": reverse("logout", request=request, format=format),
        }
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api_root),
    path("", include(router.urls)),
    path("auth/", include("userauth.urls")),
]
