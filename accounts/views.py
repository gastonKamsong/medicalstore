from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth import logout

def register(request):
    """User registration"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('pages:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    """User profile page"""
    return render(request, 'accounts/profile.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('pages:home')