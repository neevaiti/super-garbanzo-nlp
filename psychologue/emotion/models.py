from django.db import models
from django.contrib.auth.models import User

class Text(models.Model):
    # psy_id = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_id = models.IntegerField()
    # patient_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    content = models.TextField()
    emotion = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content