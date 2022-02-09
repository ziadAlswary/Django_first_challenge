from os import kill
from django.contrib import admin

# Register your models here.
from .models import Brand,Product,Kind

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Kind)
