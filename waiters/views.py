from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Waiter

class WaiterListView(LoginRequiredMixin, generic.ListView):
    template_name = "waiters/list.html"

    def get_queryset(self):
        return Waiter.objects.all()
