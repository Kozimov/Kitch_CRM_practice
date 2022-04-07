import imp
import django
from django.contrib import admin
from django.urls import path, include
from leads.views import HomeView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('leads/', include('leads.urls', namespace="leads")),
    path('login/', LoginView.as_view(), name="login"),
]
