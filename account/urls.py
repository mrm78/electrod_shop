from django.urls import path
from .views import sign_in, sign_up

urlpatterns = [
    path('up', sign_up, name='sign_up'),
    path('in', sign_in, name='sign_in')
]