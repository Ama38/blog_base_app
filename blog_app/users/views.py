from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

from users.forms import CustomUserCreationForm, CustomUserLoginForm


@login_required
def home_page_view(request):
    return render(request, 'users/home_page.html')


def register_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('register-page'))
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect(reverse('home-page'))

    else:
        form = CustomUserCreationForm()
    return render(request, 'users/login.html', context={"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect(reverse('home-page'))
    else:
        form = CustomUserLoginForm()
    return render(request, 'users/register.html', context={"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse('home-page'))



