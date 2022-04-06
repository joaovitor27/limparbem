from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.Userlogin, name='login'),
    path('sair/', views.userlogout, name='logout'),
]
