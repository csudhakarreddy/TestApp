from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return  render(request,"index.html")
def home(request):
    # Register user details
    if request.method == "POST" and 'btnSignUp' in request.POST:
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(username)
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('/')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_active = False

        myuser.save()
        messages.success(request,
                         "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('home')
    #Check login here
    if request.method == "POST" and 'btnSignIn' in request.POST:
        username = request.POST['username']
        pass1 = request.POST['loginpass1']
        print(username)

        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            print(username)
            login(request, user)
            username = user.username
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index", {"username": username})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    #Check logout here
    if request.method == "POST" and 'btnSignOut' in request.POST:
        auth.logout(request)
        messages.success(request, "Logged Out Successfully!!")
        return redirect('view.html')

    return render(request, "home.html")

def policy(request):
    return render(request,"policy.html")

from django.http import JsonResponse
import json

def process_form_data(request):
    if request.method == 'POST':
        form_data = json.loads(request.POST.get('formData'))

        # Process form_data as needed

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

def view_with_forms(request):
    return render(request, 'common_template.html', context={},)