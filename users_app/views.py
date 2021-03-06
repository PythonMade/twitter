from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You may log in.')
        return redirect('tweets-app-home')
    else:
        context = {
            'form': UserRegisterForm()
        }
        return render(request, 'users_app/register.html', context)
