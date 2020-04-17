from django.contrib import admin

# Register your models here.
from .models import HomeWork, discuss, information


admin.site.register(HomeWork)
admin.site.register(discuss)
admin.site.register(information)