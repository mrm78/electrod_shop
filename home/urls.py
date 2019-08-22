from django.urls import path
from .views import home, order_view, cart, edit_cart, send_cart
from .models import product

urlpatterns = [
    path('', home, name='home'),
    path('order/<str:ID>', order_view, name="order"),
    path('cart/<str:ID>', cart, name='cart'),
    path('edited_cart/<str:del_or_edit>/<str:ID>', edit_cart, name='edit_cart'),
    path('send_cart', send_cart, name='send_cart'),
]