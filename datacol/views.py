from django.shortcuts import render, HttpResponse
from .models import Metrics_view
# Create your views here.

def index(request):
    sql_res = Metrics_view.objects.all()
    return render(request, template_name='viz.html', context={'sql_res':sql_res})