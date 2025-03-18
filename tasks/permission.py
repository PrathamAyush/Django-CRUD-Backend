from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsOwner(permissions.BasePermission):
    
    # Custom permission to allow only task owner to edit or delete it.
    
    def has_object_permission(self, request, view, obj):
        # Read permissions (GET) allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions (PUT, DELETE) only for task owner
        if obj.user == request.user:
            return True
        
        raise PermissionDenied({"message":"You are unautrorise to do the same"})
