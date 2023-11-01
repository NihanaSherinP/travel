from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        passw=request.POST['passw']
        user=auth.authenticate(username=username,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def regis(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        passw = request.POST['passw']
        cpassw = request.POST['cpassw']
        if passw==cpassw:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username exist")
                return redirect('regis')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email exist")
                return redirect('regis')
            else:
                user=User.objects.create_user(username=username,password=passw,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('regis')
        return redirect('/')


    return render(request,'register.html')