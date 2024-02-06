
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)

    def __str__(self):
        return self.user.username
    
class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # You can add additional fields such as image or video if needed

    def __str__(self):
        return f'Content by {self.user.username} on {self.created_at.strftime("%Y-%m-%d %H:%M")}'
