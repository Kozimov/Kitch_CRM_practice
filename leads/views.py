from multiprocessing import context
from re import template
from django.shortcuts import redirect, render , reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import *

class HomeView(TemplateView):
    template_name = "home.html"


class ListsView(ListView):
    template_name = "leads_lists.html"
    queryset = models.Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = "details.html"
    queryset = models.Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
    template_name = "create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lists")

class LeadUpdateView(UpdateView):
    template_name = "update.html"
    form_class = LeadModelForm
    queryset = models.Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lists")
 
class LeadDeleteView(DeleteView):
    template_name = "delete.html"
    queryset = models.Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lists")