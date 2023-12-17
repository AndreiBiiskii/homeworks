from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from commits.views import CommentViewSet

router = DefaultRouter()
router.register('comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
