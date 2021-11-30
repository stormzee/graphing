from django.shortcuts import render, HttpResponse
from .models import Metrics_view
# Create your views here.

def index(request):
    sql = Metrics_view.objects.all()
    return render(request, template_name='viz.html', context={'sql':sql})