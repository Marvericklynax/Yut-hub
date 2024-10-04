from django.db import models
from users.models import User

class Mentorship(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentee')
    created_at = models.DateTimeField(auto_now_add=True)
