from django.urls import path
from .views import index, login_view, signup_view, about, service

urlpatterns = [
    path("", index, name = "index"),
    path("login/", login_view, name = "login"),
    path("signup/", signup_view, name = "signup"),
    path("about/", about, name = "about"),
    path("service/",service, name = "service")
]