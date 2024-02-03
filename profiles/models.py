
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)

    def __str__(self):
        return self.user.username
