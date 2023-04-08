from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login
from .forms import SigupForm


def startpage(request):
    return render(request, 'chat/startpage.html')



def signup(request):
    form = SigupForm()
    if request.method == 'POST':
        form = SigupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return reverse('chat:start-page')
    return render(request, 'chat/signup.html', {'form': form})