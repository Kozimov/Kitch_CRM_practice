from django.urls import path
from .views import *


app_name = "waiters"

urlpatterns = [
    path('', WaiterListView.as_view(), name="waiter-list"),
    path('create-waiters/', WaiterCreateView.as_view(), name="waiter-create"),
]