from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserRegisterForm, UserLoginForm, ContentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import UserProfile
# TODO: MAKE + BUTTON IN THE BUCKET, STYLE SLIPS, MOVE LOGOUT IN PROGILE AND MAKE NAV GO TO PROFILE
@login_required
def edit_user_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # If UserProfile doesn't exist, create it
        UserProfile.objects.create(user=request.user)
        profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('user_login')  
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def create_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)  
            content.user = request.user  
            content.save() 
            return redirect('home')
    else:
        form = ContentForm()
    return render(request, 'create_content.html', {'form': form})

@login_required
def home(request):
    user = request.user
    content = user.content.all()
    return render(request, 'home.html', {'user': user, 'content':content})


