from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api import views
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token 

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
schema_view = get_schema_view(title=' MYAPI')

# Wire up our API using automatic URL routing.

urlpatterns = [
   
    path('schema/', schema_view),
    path('', views.api_root),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
     
    
 ]