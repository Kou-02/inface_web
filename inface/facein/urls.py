from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('facerec/',views.facerec,name='facerec'),
    path('login/',views.login,name='signin'),
    path('redire/',views.redire,name='redire'),
    path('student/',views.student,name='student'),
    path('staff/',views.staff,name='staff')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)