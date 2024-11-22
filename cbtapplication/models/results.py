from django.db import models
from datetime import datetime
from . import ExamSubject
from django.contrib.auth.models import User

class Result(models.Model):
    exam_subject = models.ForeignKey(ExamSubject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    grade = models.CharField(max_length=5)
    created_at = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.exam_subject.subject}"