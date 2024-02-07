
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
    
    def total_likes(self):
        return self.likes.count()

    def is_liked_by_user(self, user):
        return self.likes.filter(user=user).exists()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey('Content', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content')  # Ensure a user can only like a content once

    def __str__(self):
        return f'{self.user.username} likes {self.content.id}'