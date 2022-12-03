from django.urls import path
from .views import *

urlpatterns = [
    path("", indexPageView, name="index"),
    path("new-flight", newflight, name="new-flight"),
    path("update-flight/<int:flightid>",updateflight, name="update-flight"),
    path("delete-flight/<int:flightid>", deleteflight, name="delete-flight"),
    path("incomplete-entries", incompletePageView, name="incomplete-entries"),
    path("401", unauthorizedPageView, name="401"),
    path("404", errorPageView, name="404"),
    path("500", serverPageView, name="500"),
    path("login",loginPageView, name="login"),
    path("password",passwordPageView, name="password"),
    path("charts", chartsPageView, name="charts"),
    path("entries", entriesPageView, name="entries"),
    path("register", registerPageView, name="register"),
]                  
            