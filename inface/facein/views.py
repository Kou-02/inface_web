from django.shortcuts import redirect, render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators import gzip
from django.contrib.auth.models import User
from .models import *
from django.core.mail import EmailMessage
#import sqlite3
from sre_constants import SUCCESS
from tabnanny import check
#import cv2
import numpy as np
import face_recognition as fc
#import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
#import cv2
#from django.contrib.auth.models import User
#from .models import *
#from django.core.mail import EmailMessage
#import sqlite3
#from sre_constants import SUCCESS
#from tabnanny import check
##import cv2
#import numpy as np
#import face_recognition as fc
#import os
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate,login
#from django.contrib.auth.forms import UserCreationForm

@gzip.gzip_page

# Create your views here.

def index(request):
    return render(request, 'facein/index.html')

#def facerec(request):
    


def login(request):
    form = UserCreationForm()
    return render(request, "facein/login.html",)

#def logout(request):

def profile(request):
    return render(request,"facein/profile.html")