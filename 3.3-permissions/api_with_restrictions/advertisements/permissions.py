from rest_framework.permissions import BasePermission

from advertisements.models import Advertisement


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator or request.user.is_staff

    # def has_permission(self, request, view):
    #     # count = Advertisement.objects.filter(creator=request.user.id, status='OPEN').count()
    #     # if (request.method == 'POST') and (count > 10):
    #     #     return False
    #     return True
