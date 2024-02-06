from django.urls import path
from .views import edit_user_profile, register, user_login, home, create_content

urlpatterns = [
    path('edit/', edit_user_profile, name='edit_user_profile'),
    path('new_slip/', create_content, name='new_slip'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('', home, name='home'),
]