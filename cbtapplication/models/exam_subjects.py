from django.db import models
from datetime import datetime
from . import Subject

class ExamSubject(models.Model):
    CLASS_YEAR_CHOICES = {
        "1":"SS1",
        "2":"SS2",
        "3":"SS3"
    }
    DEPARTMENT_CHOICES = {
        "all":"All Departments",
        "science":"Science",
        "business":"Business",
        "humanity":"Humanity"
    }
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    class_year = models.CharField(max_length=100, choices=CLASS_YEAR_CHOICES, verbose_name="Class")
    is_active = models.BooleanField(max_length=10, default=False, verbose_name="Activate Exam")
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"SS {self.class_year} {self.subject.name}"