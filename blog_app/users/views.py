from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

from users.forms import CustomUserCreationForm, CustomUserRegisterForm


@login_required
def home_page_view(request):
    return render(request, 'users/home_page.html')


def login_view(request):
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


def register_view(request):
    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password')
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            user = form.save()
            login(request, user)
    else:
        form = CustomUserRegisterForm()
    return render(request, 'users/register.html', context={"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse('home-page'))



