from django.urls import path, include

urlpatterns = [
    path('api/', include('users.urls')),
    path('api/', include('mentorship.urls')),
]