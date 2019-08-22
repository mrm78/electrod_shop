from django.shortcuts import render, redirect
from .models import user
from django.contrib import auth

def sign_up(req):
    auth.logout(req)
    if req.method=='POST':
        if not(req.POST['name'] and req.POST['family'] and req.POST['password'] and req.POST['phone'] and req.POST['address'] and req.POST['username']):
            return render(req, 'sign_up.html', {'error':'!لطفا همه ی قسمت ها را پر کنید'})
        User = user.objects.filter(username=req.POST['username'])
        if User:
            return render(req, 'sign_up.html', {'error':'!این نام کاربری قبلا ثبت شده است'})
        else:
            User = user.objects.create_user(username=req.POST['username'], password=req.POST['password'], first_name=req.POST['name'], last_name=req.POST['family'], phone=req.POST['phone'], address=req.POST['address'])
            auth.login(req, User)
            return redirect('home')

    else:
        return render(req, 'sign_up.html')


def sign_in(req):
    if req.method == 'POST':
        if not(req.POST['password'] and req.POST['username']):
            return render(req, 'sign_in.html', {'error':'!لطفا همه ی قسمت ها را پر کنید'})
        User = auth.authenticate(username=req.POST['username'], password=req.POST['password'])
        if User:
            auth.login(req, User)
            return redirect('home')
        else:
            return render(req, 'sign_in.html', {'error':'!نام کاربری یا رمز عبور اشتباه است'})

    else:
        return render(req, 'sign_in.html')






