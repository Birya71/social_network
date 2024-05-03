from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            print(view)
            return request.user == obj.user
    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS: #or obj.author == request.user
    #         return True
    #     else:
    #         return request.user == obj.user

        # return (
        #         request.method in permissions.SAFE_METHODS
        #         or obj.author == request.user
        # )
