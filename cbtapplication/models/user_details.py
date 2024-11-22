from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    class_year = models.CharField(max_length=5, blank=True)
    department = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} {self.user.last_name} {self.role}"

# username: olacbtmoderator
# password: cbtmoderator