from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.userRegister, name="register"),
    path("login/", views.userLogin, name="login"),
    path("logout/", views.userLogout, name="logout"),
]
