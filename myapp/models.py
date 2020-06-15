from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    gender = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    designation = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{0}".format(self.user_id)
