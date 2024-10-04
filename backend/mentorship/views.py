from rest_framework import viewsets
from .models import Mentorship
from .serializers import MentorshipSerializer

class MentorshipViewSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer