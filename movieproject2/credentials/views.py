from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                messages.success(request,f"welcome to movie platform, {username}!")
                return redirect('login')



        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def profile(request):
    user=request.user
    return render(request,'profile.html',{'user':user})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return redirect('profile')
    return render(request, 'edit_profile.html', {'user': user})
