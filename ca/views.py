from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/old-admin/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.info(request, 'Account not found')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = authenticate(username=username, password=password)

        if user and user.is_superuser:
            login(request, user)
            return redirect('http://127.0.0.1:8000/old-admin/')
        else:
            messages.info(request, 'Invalid password or not a superuser')

    return render(request, 'ca/login.html')