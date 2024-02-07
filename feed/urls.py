from django.urls import path
from .views import feed, like_content

urlpatterns = [
    path('', feed, name='feed'),
    path('like_content/<int:content_id>/', like_content, name='like_content'),
]