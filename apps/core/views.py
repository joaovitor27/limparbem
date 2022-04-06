from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import UserForm
# Create your views here.

def add_user(request):
    template_name = 'login/add_user.html'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
    
    form = UserForm()
    context = {'form':form}

    return render(request, template_name, context)


def Userlogin(request):
    template_name = 'login/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.ERROR(request, 'Usuário ou Senha Inválidos!')

    context = {}
    return render(request, template_name, context)


@login_required(login_url='/login')
def userlogout(request):
    logout(request)
    return redirect('home:login')


@login_required(login_url='/login')
def home(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)