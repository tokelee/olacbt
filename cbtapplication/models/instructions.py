from django.db import models
from datetime import datetime

class Instruction(models.Model):
    instruction = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)
