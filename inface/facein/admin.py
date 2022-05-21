import profile
from django.contrib import admin
from .models import Profile, attandance,std_details,attandance
# Register your models here.

admin.site.register(Profile)
admin.site.register(std_details)
admin.site.register(attandance)