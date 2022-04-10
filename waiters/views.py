from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import WaiterModelForm
from leads.models import Waiter

class WaiterListView(LoginRequiredMixin, generic.ListView):
    template_name = "waiters/list.html"

    def get_queryset(self):
        return Waiter.objects.all()


class WaiterCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "waiters/create.html"
    form_class = WaiterModelForm

    def get_success_url(self):
        return reverse("waiters:waiter-list")

    def form_valid(self, form):
        waiter = form.save(commit=False)
        waiter.profil = self.request.user.userprofil
        waiter.save()
        return super(WaiterCreateView, self).form_valid(form)