from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    message = 'Tienes que ser el propietario del recurso.'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_admin
