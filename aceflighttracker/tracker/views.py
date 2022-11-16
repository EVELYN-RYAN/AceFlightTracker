from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return HttpResponse("Start of Project")