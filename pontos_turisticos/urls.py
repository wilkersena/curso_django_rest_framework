"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from resources.api.viewsets import ResourceViewSet
from reviews.api.viewsets import ReviewViewSet
from addresses.api.viewsets import AddressViewSet
from comments.api.viewsets import CommentViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'resource', ResourceViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'address', AddressViewSet)
router.register(r'comment', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
