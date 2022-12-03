from django.urls import path
from .views import *

urlpatterns = [
    path("", indexPageView, name="index"),
    path("new-entry", newentryPageView, name="new-entry"),
    path("incomplete-entries", incompletePageView, name="incomplete-entries"),
    path("401", unauthorizedPageView, name='401'),
    path("404", errorPageView, name='404'),
    path("500", serverPageView, name='500'),
    path("login",loginPageView, name='login'),
    path("password",passwordPageView, name='password'),
    path("charts", chartsPageView, name='charts'),
    path("entries", entriesPageView, name='entries'),
    path("register", registerPageView, name='register')          
]                  
            