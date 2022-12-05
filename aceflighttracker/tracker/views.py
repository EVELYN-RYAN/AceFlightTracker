from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Flight
from datetime import datetime
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
import csv
from .functions import *


# Create your views here.
def indexPageView(request):
    flight = Flight.objects.all().order_by('-flightid')
    n = datetime.now()
    m = int(n.strftime('%m'))
    y = int(n.strftime('%Y'))
    monthHours = 0
    for r in flight:
        d = datetime.strptime(r.date,'%m/%d/%y')
        if r.total is not None:
            if d >= datetime(y,m,1):
                monthHours += r.total
    context ={
        'flight': flight,
        'monthHours': monthHours
    }
    return render(request, 'aceflighttracker/index.html',context)

def incompletePageView(request):
    incomplete_list = Flight.objects.all()
    incomplete_list = Flight.objects.filter(from_field=None, to=None)
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

# ================= ENTRIES RELATED VIEWS =====================
def entriesPageView(request):
    flight = Flight.objects.all().order_by('-flightid')
    context = {
        'flight': flight,
    }
    return render(request,'aceflighttracker/entries.html',context)

def export_csv(request):
    flight = Flight.objects.all().order_by('-flightid')
    r = HttpResponse('')
    r['Content-Disposition'] = 'attachment; filename=flight_tracker.csv'
    writer = csv.writer(r)
    writer.writerow(['FlightId','Date','Days','FlightNum','AircraftId','From','To',
    'Out','Off','On','In','TOTAL','Night','IMC','PilotFlying','ApproachType','DayT/O','DayLdg','NightT/O','NightLdg','Remarks'])
    fields = flight.values_list('flightid','date','days','flightnum','aircraftid','from_field','to','out','off','on','in_field','total','night','imc','pilotflying','approachtype','dayt_o','dayldg','nightt_o','nightldg','remarks')
    for f in fields:
        writer.writerow(f)
    return r

def chartsPageView(request):
    return render(request,'aceflighttracker/charts.html')

# ================= CRUD RELATED VIEWS =====================
@csrf_protect  
def newflight(request):
    new = Flight()
    n = datetime.now()
    new.date = n.strftime("%m/%d/%y")
    new.save()
    new.date = n.strftime("%Y-%m-%d")
    # new.out = n.strftime("%HH:%MM")
    context = {
        'new': new
    }
    return render(request,'aceflighttracker/new-entry.html',context)

@csrf_protect    
def updateflight(request, flightid):
    if request.method == 'POST':
        r = request.POST
        flight = Flight.objects.get(flightid=flightid)
        date = datetime.strptime(r.get('date'),"%Y-%m-%d")
        flight.date = date.strftime("%m/%d/%y")
        flight.days = string_to_int(r.get('days'))
        flight.flightnum = string_to_int(r.get('flightnum'))
        flight.aircraftid = check_null(r.get('aircraftid'))
        flight.from_field = check_null(r.get('from_field'))
        flight.to = check_null(r.get('to'))
        flight.out = time_to_integer(r.get('out'))
        flight.off = time_to_integer(r.get('off'))
        flight.on = time_to_integer(r.get('on'))
        flight.in_field = time_to_integer(r.get('in_field'))
        #I would love to know how to calculate total and night
        flight.total = string_to_float(r.get('total'))
        flight.night = string_to_float(r.get('night'))
        flight.imc = string_to_float(r.get('imc'))
        flight.pilotflying = int(r.get('pilotflying'))
        flight.approachtype = check_null(r.get('approachtype'))
        flight.dayt_o = int(r.get('dayt_o'))
        flight.dayldg = int(r.get('dayldg'))
        flight.nightt_o = int(r.get('nightt_o'))
        flight.nightldg = int(r.get('nightldg'))
        flight.remarks = check_null(r.get('remarksflight'))
        flight.save()

        if 'save' in r:
            request = HttpRequest()
            request.method = 'GET'
            return updateflight(request,flightid)
        else:
            return indexPageView(request)
    if request.method == 'GET':
        flight = Flight.objects.get(flightid=flightid)
        d = datetime.strptime(flight.date,"%m/%d/%y")
        flight.date = d.strftime("%Y-%m-%d")
        flight.out = int_to_time(flight.out)
        flight.off = int_to_time(flight.off)
        flight.on = int_to_time(flight.on)
        flight.in_field = int_to_time(flight.in_field)
        context = {
            'flight':flight
        }
        return render(request,'aceflighttracker/update-entry.html',context)
    
def deleteflight(request, flightid):
        r = request
        flight = Flight.objects.get(flightid=flightid)
        flight.delete()
        prev_page = r.environ['HTTP_REFERER']
        return HttpResponseRedirect(prev_page)