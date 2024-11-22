from django.db import models
from datetime import datetime

class Subject(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.name}"