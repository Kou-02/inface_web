from re import T
from tracemalloc import start
import cv2 #koushik
from msilib.schema import AdminExecuteSequence
from django.shortcuts import redirect, render
from django.http import HttpResponse, StreamingHttpResponse
from django.template import engines
from django.views.decorators import gzip
from django.contrib.auth.models import User
from .models import Profile as pro
from django.core.mail import EmailMessage
import sqlite3
from sre_constants import SUCCESS
from tabnanny import check
import numpy as np
import face_recognition as fc #koshik
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.conf.urls.static import static
from django.contrib.auth.models import User
from .models import *
from django.core.mail import EmailMessage
from sre_constants import SUCCESS
from tabnanny import check
import numpy as np
import face_recognition as fc
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.forms import UserCreationForm
import time
from playsound import playsound

cwd = os.getcwd()
music = os.path.join(cwd,'done.mp3')

@gzip.gzip_page

# Create your views here.

def index(request):
    return render(request, 'facein/index.html')

def facerec(request):
    start = 2
    end = 5
    i=start
    count=pro.objects.all().count()
    print(count)
    while True:
        if i <=end:
            loc=pro.objects.filter(id= i).values_list('Profile_picture').first()[0]
            print (loc)
            i+=1
            path=os.path.join(cwd,'media',loc).replace("\\","/")
            img = cv2.imread(path)
            img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            facescurframe = fc.face_locations(img)
            encode = fc.face_encodings(img,facescurframe)
            print(encode)
            cap = cv2.VideoCapture(0)
            break_out_flag = False

                #
            SUCESS,img = cap.read()
            imgs = cv2.resize(img,(0,0),None,0.25,0.25)
            imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
            facescurframe = fc.face_locations(img)
            encode2=fc.face_encodings(img,facescurframe)
            for encodeface,faceloc in zip(encode2,facescurframe):
                match = fc.compare_faces(encode,encodeface)
                if match[0] == True:
                    print("hehehe")
                    print('done')
                    playsound(music)
                    print()
                    time.sleep(2.4)
                    print(music)
                    
                    break

        else:
            i=start
                    
            #you where going to get the sql data to start the face scanning


    return render(request,"facein/facerec.html", {'title': "face",'id':id})

 
    
def redirect(request):
    return render(request,"/facein/redirect.html")

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
