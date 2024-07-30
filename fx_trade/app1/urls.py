from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('account',views.account,name='account'),
    path('login',views.login,name='login'),
    path('trade',views.trade,name='trade'),
]
