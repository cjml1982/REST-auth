"""DRFjwt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from django.contrib import admin
#import demo.views as demo_views 
from rest_framework.routers import DefaultRouter
#import django.rest_auth
#import django.rest_auth.registration

#router = DefaultRouter()
#router.register(r'task', demo_views.TaskViewSet)
#router.register(r'user', demo_views.UserViewSet)
from django.conf.urls import url
from .views import hello_world
from django.views.generic import TemplateView
from rest_framework_jwt import views
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class MockView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return HttpResponse('mockview-get')

    def post(self, request):
        return HttpResponse('mockview-post')

urlpatterns = [
#    url(r'^.*$', TemplateView.as_view(template_name='index.html')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),
#    url(r'^api-register/', demo_views.CreateUserView.as_view()),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^hello/', hello_world, name="hello_world"),
    url(r'^jwt/$', MockView.as_view(authentication_classes=[JSONWebTokenAuthentication])),
]
