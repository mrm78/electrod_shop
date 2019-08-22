from django.shortcuts import render, redirect
from .models import product, brands, types, order
from account.models import registered_orders
from django.contrib import auth
import requests


def home(req):
    shown_brands = brands.objects.filter(display_on_home='بله')
    shown_types = types.objects.filter(display_on_home='بله')
    products_on_top = []
    q = ''
    if req.method == 'POST':
        q = req.POST['q']
        if req.POST['form'] == 'names':
            for prdct in product.objects.all():
                if q in prdct.name:
                    products_on_top.append(prdct)
        elif req.POST['form'] == 'types':
            products_on_top = types.objects.get(name=q).product_set.all()
        elif req.POST['form'] == 'brands':
            products_on_top = brands.objects.get(name=q).product_set.all()

    products_on_bottom = product.objects.all()
    return render(req, 'home.html', {'products_on_top':products_on_top, 'products_on_bottom':products_on_bottom, 'q':q, 'shown_types':shown_types, 'shown_brands':shown_brands, 'brands':brands.objects.all(), 'types':types.objects.all()})


def order_view(req, ID):
    PRODUCT = product.objects.get(id=int(ID))
    return render(req, 'order.html', {'product':PRODUCT})


def cart(req, ID):
    if req.method == 'POST':
        Amount = req.POST['amount']
        ordered_product = product.objects.get(id=int(ID))
        Order = order(size=ordered_product.size, amount=Amount, product=ordered_product)
        Order.save()
        auth.get_user(req).cart.add(Order)
    return render(req, 'cart.html')


def edit_cart(req, del_or_edit, ID):
    ORDER = order.objects.get(id=int(ID))
    if del_or_edit == 'delete':
        ORDER.delete()
        return redirect('cart', ID='a')
    elif del_or_edit == 'edit':
        if req.method == 'POST':
            Amount = req.POST['amount']
            ORDER.amount = Amount
            ORDER.save()
            return redirect('cart', ID='a')
        else:
            return render(req, 'edit_order.html', {'order':ORDER})
    


def send_cart(req):
    if req.method == 'POST':
        #making cart message
        message = 'سفارشات:'
        user = auth.get_user(req)
        counter = 1
        for order in user.cart.all():
            message += f'\n {counter}: {order.product.name} : {order.amount} {order.product.Type.unit}'
            counter += 1
        message += f'\n نام: {user.first_name} {user.last_name}'
        message += f'\n تلفن: {req.POST["phone"]}'
        message += f'\n آدرس: {req.POST["address"]}'
        #sending message via SMS
        jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDIzNCIsImV4cCI6MTg4MjA3OTYzOSwiaXNzIjoiQml0ZWwiLCJhdWQiOiJCaXRlbCJ9.HhhSzRZ7k2vo4PTkLXOsHj9KwbRNl9Z7MAl5rqOHNWk'
        phone = '09909499767'
        headers = {
            'Authorization': 'Bearer ' + jwt_token,
            'content-type': 'application/json'
        }
        payload = {
            'phoneNumber': phone,
            'message': message
        }
        if user.cart.all():
            response = requests.post('https://api.bitel.rest/api/v1/sms/single',json=payload, headers=headers)
            if response.status_code == 200:
                registered_order = registered_orders(user=user)
                registered_order.save()
                registered_order.cart.set(user.cart.all())
                user.cart.clear()
                return render(req, 'send_cart.html', {'message':'سفارش شما ثبت گردید. جهت هماهنگی بیشتر با شما تماس گرفته خواهد شد.', 'type':'alert-success'})
            else:
                return render(req, 'send_cart.html', {'message':'مشکلی در ثبت سفارش بوجود آمده. لطفا دوباره تلاش کنید.', 'type':'alert-danger'})
        else:
            return render(req, 'send_cart.html',{'message':'!!سبد خرید شما خالی میباشد', 'type':'alert-warning'})
    else:
        return render(req, 'send_cart.html')