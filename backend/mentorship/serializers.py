from .models import Mentorship
from rest_framework import serializers


class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = '__all__'