from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserDetail(models.Model):
    ROLE_CHOICES = {
        'student': "Student",
        'moderator': "Moderator"
    }
    CLASS_YEAR_CHOICES = {
        "1":"SS1",
        "2":"SS2",
        "3":"SS3"
    }
    DEPARTMENT_CHOICES = {
        "science":"Science",
        "business":"Business",
        "humanity":"Humanity"
    }
    class_year = models.CharField(max_length=5, blank=True, choices=CLASS_YEAR_CHOICES)
    department = models.CharField(max_length=50, blank=True, choices=DEPARTMENT_CHOICES)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    is_computer_literate = models.BooleanField(max_length=10, default=False, verbose_name="I am computer literate")
    dob = models.DateField(verbose_name="Date of birth", blank=True, default=datetime(2006,1,1))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user.username} {self.user.last_name} {self.role}"

# username: olacbtmoderator
# password: cbtmoderator