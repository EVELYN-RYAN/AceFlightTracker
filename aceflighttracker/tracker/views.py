from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Flight
from datetime import datetime
from .functions import *

# Create your views here.
def indexPageView(request):
    flight = Flight.objects.all().order_by('-flightid')
    context ={
        'flight': flight
    }
    return render(request, 'aceflighttracker/index.html',context)

def incompletePageView(request):
    incomplete_list = Flight.objects.all()
    incomplete_list = Flight.objects.filter(from_field= None, to = None)
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

def newflight(request):
    new = Flight()
    n = datetime.now()
    new.date = n.strftime("%m/%d/%y")
    new.out = int(n.strftime("%H%M"))
    new.save()
    new.date = n.strftime("%Y-%d-%m")
    # new.out = n.strftime("%HH:%MM")
    context = {
        'new': new
    }
    return render(request,'aceflighttracker/new-entry.html',context)
    
def updateflight(request, flightid):
    if request.method == 'POST':
        r = request.POST
        flight = Flight.objects.get(flightid=flightid)

        date = datetime.strptime(r.get('date'),"%Y-%m-%d")
        flight.date = date.strftime("%m/%d/%y")
        flight.days = int(r.get('days'))
        flight.flightnum = r.get('flightnum')
        flight.aircraftid = r.get('aircraftid')
        flight.from_field = r.get('from_field')
        flight.to = r.get('to')
        flight.out = time_to_integer(r.get('out'))
        flight.off = time_to_integer(r.get('off'))
        flight.on = time_to_integer(r.get('on'))
        flight.in_field = time_to_integer(r.get('in_field'))
        #I would love to know how to calculate total and night
        flight.total = float(r.get('total'))
        flight.night = float(r.get('night'))
        flight.imc = float(r.get('imc'))
        flight.pilotflying = int(r.get('pilotflying'))
        flight.approachtype = r.get('approachtype')
        flight.dayt_o = int(r.get('dayt_o'))
        flight.dayldg = int(r.get('dayldg'))
        flight.nightt_o = int(r.get('nightt_o'))
        flight.nightldg = int(r.get('nightldg'))
        flight.remarks = r.get('remarksflight')
        flight.save()
        return render(request,'aceflighttracker/submitted.html')
    if request.method == 'GET':
        flight = Flight.objects.get(flightid=flightid)
        context = {
            'flight':flight
        }
        return render(request,'aceflighttracker/update-entry.html')
    
def deleteflight(request, flightid):
        flight = Flight.objects.get(flightid=flightid)
        flight.delete()
        return indexPageView(request)