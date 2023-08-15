from django.urls import path
from .. import views


urlpatterns = [
    path("company/", views.company_list, name="company_list"),
    path("login/", views.Login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("sessionTester/", views.sessionTester, name="sessionTester"),
]
