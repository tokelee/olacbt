from django.db import models
from datetime import datetime
from . import ExamSubject

class Question(models.Model):
    question = models.TextField()
    diagram = models.ImageField(upload_to="uploads/", blank=True) #pillow is required
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    answer = models.CharField(max_length=1)
    exam_subject = models.ForeignKey(ExamSubject, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f"SS {self.exam_subject.class_year} - {self.question}"