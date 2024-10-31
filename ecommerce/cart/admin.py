from django.contrib import admin

from cart.models import Cart,Payment,Order_details
from django.http import HttpResponse
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Order_details)
