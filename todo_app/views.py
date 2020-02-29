from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

# Create your views here.
from base_user.forms import MyUserCreationForm
from base_user.models import MyUser
from todo_app.forms import LoginForm, AddKey


def index(request):
    return render(request, 'index.html')


def register(request):
    context = {}
    form = MyUserCreationForm
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('index')
        else:
            messages.error(request, form.errors)
    context['form'] = form

    return render(request, 'log-reg/register.html', context)


def login(request):
    context = {}
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.error(
                    request, "Username or Password inValid"
                )

    context['form'] = form
    return render(request, 'log-reg/login.html', context)


def addkey(request):
    context = {}
    context['form'] = AddKey()

    if request.method == "POST":
        form = AddKey(request.POST)
        if form.is_valid():
            port = request.POST.get('port')
            form.instance.port = port
            username = form.cleaned_data.get('user')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            Users=MyUser.objects.filter(username=username,password=password)
            # print(Users)
            if user:
                # print(Users)
                form.save()
                return redirect('index')
    return render(request, 'addkey/key.html', context)
