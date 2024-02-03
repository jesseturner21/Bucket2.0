from django.urls import path
from .views import edit_user_profile, register, user_login, home

urlpatterns = [
    path('edit_profile/', edit_user_profile, name='edit_user_profile'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('', home, name='home'),
]