from django.shortcuts import render

def home(request):
    return render(request, 'tweets_app/home.html')
