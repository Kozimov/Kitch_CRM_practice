from django.urls import path
from .views import WaiterListView


app_name = "waiters"

urlpatterns = [
    path('', WaiterListView.as_view(), name="waiter-list")
]