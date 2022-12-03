from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Flight

# Create your views here.
def indexPageView(request):
    flight = Flight.objects.all().order_by('-flightid')
    context ={
        'flight': flight
    }
    return render(request, 'aceflighttracker/index.html',context)

def newentryPageView(request):
    return render(request, 'aceflighttracker/new-entry.html')

def incompletePageView(request):
    incomplete_list = Flight.objects.filter(to = None)
    context ={
        'flight': incomplete_list
    }
    return render(request, 'aceflighttracker/incomplete-entries.html',context)

def unauthorizedPageView(request):
    return render(request,'aceflighttracker/401.html')

def errorPageView(request):
    return render(request,'aceflighttracker/404.html')

def serverPageView(request):
    return render(request,'aceflighttracker/500.html')

def loginPageView(request):
    return render(request,'aceflighttracker/login.html')

def passwordPageView(request):
    return render(request,'aceflighttracker/password.html')

def registerPageView(request):
    return render(request,'aceflighttracker/register.html')

def entriesPageView(request):
    flight = Flight.objects.all().order_by('-flightid')
    context = {
        'flight': flight
    }
    return render(request,'aceflighttracker/entries.html',context)

def chartsPageView(request):
    return render(request,'aceflighttracker/charts.html')
