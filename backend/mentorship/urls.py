from django.urls import path, include
from .views import MentorshipViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mentorships', MentorshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

