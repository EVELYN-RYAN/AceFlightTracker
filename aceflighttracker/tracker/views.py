from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'aceflighttracker/index.html')

def punchclockPageView(request):
    return render(request, 'aceflighttracker/punchclock.html')

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
    return render(request,'aceflighttracker/entries.html')

def chartsPageView(request):
    return render(request,'aceflighttracker/charts.html')
