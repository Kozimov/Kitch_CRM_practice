import random
from urllib import request
from django.views import generic
from django.shortcuts import reverse
from django.core.mail import send_mail
from leads.models import Agent, UserProfile
from .mixins import OrganisorAndLoginRequiredMixin
from .forms import AgentModelForm

class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agents_lists.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = organisation)

class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agents_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_organisor = False
        user.is_agent = True
        user.set_password(f"{random.randint(0, 1000)}")
        user.save()
        Agent.objects.create(
            user = user,
            organisation = self.request.user.userprofile
        )
        send_mail(
            subject="Bu Agent yaratilingan",
            message="Yangi Agent yaratilgan",
            from_email="test@test.com",
            recipient_list=[user.email],
        )
        # agent.organisation = self.request.user.userprofile
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agents_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = organisation)


class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agents_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = organisation)


    def get_success_url(self):
        return reverse("agents:agent-list")

class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agents_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = organisation)

    def get_success_url(self):
        return reverse("agents:agent-list")