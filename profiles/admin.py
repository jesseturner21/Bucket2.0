from django.contrib import admin
from .models import UserProfile, Content, Like

admin.site.register(UserProfile)
admin.site.register(Content)
admin.site.register(Like)