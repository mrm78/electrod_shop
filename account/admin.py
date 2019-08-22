from django.contrib import admin
from .models import user, registered_orders

admin.site.register(user)
admin.site.register(registered_orders)
