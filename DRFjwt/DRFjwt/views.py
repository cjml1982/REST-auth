
from django.http.response import JsonResponse
from rest_framework import permissions
from rest_framework_jwt import authentication
from .permissions import CustomPermission

def hello_world(request):
#permission_classes = (permissions.IsAuthenticated, )
#    permission_classes = (IsAuthentication,) 
#    permission_classes = (CustomPermission,)
    authentication_classes = (JSONWebTokenAuthentication,)
    return JsonResponse({"message": "hello world!"})

#class YourView(APIView)
#    permission_calsses = (CustomPermission,)
