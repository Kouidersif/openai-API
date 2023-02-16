from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from .forms import UserLoginForm
urlpatterns=[
    path("", views.index, name='main'),
    path("sign-up/", views.SignUp.as_view(), name='signup'),
    path("delete/", views.DeleteHistory, name='deleteChat'),
    path("logout/", LogoutView.as_view(next_page='main'), name="logout"),
    path("login/", LoginView.as_view(next_page='main', template_name="login.html", form_class = UserLoginForm), name="login"),
]