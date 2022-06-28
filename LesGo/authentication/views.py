from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from authentication.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        hash_pwd = make_password(password)

        newUser = User(email=email, password=hash_pwd)
        newUser.save()

        return redirect('login')

    return render(request, 'authentication/register.html')