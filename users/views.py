from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserOurRegistration

def register(request):
    if request.method == "POST":
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} is created!')
            return redirect('shop-home')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Registration'})
