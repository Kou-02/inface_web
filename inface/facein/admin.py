import profile
from django.contrib import admin
from .models import Profile,std_details
# Register your models here.

admin.site.register(Profile)
admin.site.register(std_details)