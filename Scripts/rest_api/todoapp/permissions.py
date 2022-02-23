from rest_framework import permissions
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow only owners to edit and update
    """

    def has_object_persmission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return HttpResponse(request.user)

        return obj.owner == request.user