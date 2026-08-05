from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="users_app/login.html",
            authentication_form=LoginForm
        ),
        name="login"
    ),
    
    path(
    "logout/",
    auth_views.LogoutView.as_view(
        next_page=reverse_lazy("login")
    ),
    name="logout"
),
]