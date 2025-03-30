from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def userRegister(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username=cd["username"], password=cd["password"], email=cd["email"]
            )
            user.first_name = cd["first_name"]
            user.last_name = cd["last_name"]
            user.save()
            messages.success(
                request,
                "Registration successful! You can now log in.",
                extra_tags="alert alert-success",
            )

            return redirect("user-register")
    else:
        form = CreateUserForm()
    return render(request, "register.html", {"form": form})


def userLogin(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(
                    request, "Logged in successfuly!", "alert alert-success"
                )
                return redirect("home")
            else:
                messages.error(
                    request, "Username or Password is incorrect!", "alert alert-danger"
                )
    else:
        form = LoginUserForm()
    return render(request, "login.html", {"form": form})


def userLogout(request):
    logout(request)
    messages.success(request, "User Logged out successfully", "alert alert-success")
    return redirect("home")
