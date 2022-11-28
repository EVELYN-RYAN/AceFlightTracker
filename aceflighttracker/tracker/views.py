from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Flight

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

class HoursChartView(DetailView):
    template_name = 'components/hoursGraph.html'
    model = Flight

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Flight.objects.all()
        return context