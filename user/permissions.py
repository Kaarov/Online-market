from rest_framework.permissions import BasePermission

from user.models import *


class ManagerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == MANAGER:
            return True
        else:
            return False


class VIPPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == VIP:
            return True
        else:
            return False


class BuyerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == BUYER:
            return True
        else:
            return False
