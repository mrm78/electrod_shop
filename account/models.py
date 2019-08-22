from django.db import models
from django.contrib.auth.models import AbstractUser
from home.models import order

class user(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='تلفن')
    address = models.TextField(verbose_name='آدرس')
    cart = models.ManyToManyField(order, null=True, blank=True, verbose_name='سبد خرید')
    def total_price(self):
        total = 0
        for Order in self.cart.all():
            total += Order.total_price()
        return int(total)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = " کاربر"



class registered_orders(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='سفارش دهنده')
    cart = models.ManyToManyField(order, verbose_name='سبد خرید')
    date = models.DateTimeField(verbose_name='زمان خرید', auto_now=True)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'سفارشات ثبت شده'