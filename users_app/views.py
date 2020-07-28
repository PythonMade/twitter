from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You may log in.')
        return redirect('tweets-app-home')
    else:
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'users_app/register.html', context)
