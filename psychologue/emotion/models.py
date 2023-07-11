from django.db import models
from django.contrib.auth.models import User

class Psychologist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Text(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    content = models.TextField()
    emotion = models.CharField(max_length=100)  # Placeholder, replace with your emotion model's output
    created_at = models.DateTimeField(auto_now_add=True)
