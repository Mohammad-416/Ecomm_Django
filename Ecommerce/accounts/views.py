from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile

def register_page(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('name')
        last_name = ''
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        user_obj = User.objects.filter(username = email)
    
        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
    
        user_obj = User.objects.create(first_name = first_name, last_name = last_name, email = email, username = email)
        user_obj.set_password(password)
        user_obj.save()
        
        messages.success(request, 'An email has been sent on your mail')
        messages.warning(request, "If you can't find the email, please check the spam folder")
        
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'accounts/registration.html')

def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        user_obj = User.objects.filter(username = email)
    
        if not user_obj.exists():
            messages.warning(request, 'User Not Found.')
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Account Not Verified.')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = email, password = password)
        

        if user_obj:
            login(request, user_obj)
            return redirect("http://127.0.0.1:8000/")
         
        messages.warning(request, 'Invalid Email or Password')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/login.html')

def activate_email(request, email_token):
    try:
        
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect("http://127.0.0.1:8000/accounts/login")
    except Exception as e:
        return HttpResponse('Invalid Email Token')