from django.urls import path
from user.views import *


urlpatterns = [
    
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',user_register,name='register'),
    path('sifre-degistir/',sifre_degistir,name='sifre-degistir')
] 
