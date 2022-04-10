from django import forms
from leads.models import Waiter

class WaiterModelForm(forms.ModelForm):
    class Meta:
        model = Waiter
        fields = (
            'user',
        )