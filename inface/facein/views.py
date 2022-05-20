import cv2
from django.shortcuts import redirect, render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators import gzip
from django.contrib.auth.models import User
from .models import Profile
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
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.conf.urls.static import static

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
from django.contrib.auth import authenticate,login as auth_login
#from django.contrib.auth.forms import UserCreationForm

@gzip.gzip_page

# Create your views here.

def index(request):
    return render(request, 'facein/index.html')

def facerec(request):
    cap = cv2.VideoCapture(0)
    print ("the program is running")
    i=0
    # while i
    print (Profile.objects.id_no)
    
    #you where going to get the sql data to start the face scanning


    return render(request,"facein/facerec.html", {'title': "face",'id':id})

 
    


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        user = authenticate(username= request.POST['username'],password= request.POST['password'])
        if user is not None:

            auth_login(request, user)
            return redirect('facerec')
    
    else:
        form = AuthenticationForm(data=request.POST)

    return render(request, "facein/login.html", {'form': form})

#def logout(request):

@login_required
def profile(request):
    return render(request,"facein/profile.html")
