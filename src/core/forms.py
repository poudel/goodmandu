from django import forms
from core.models import EmailSubscription


class EmailSubscriptionForm(forms.ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ("email",)
