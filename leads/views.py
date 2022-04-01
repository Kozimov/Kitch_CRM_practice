from multiprocessing import context
from django.shortcuts import render
from . import models

def home(request):
    leads = models.Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, 'index.html', context)