from django import forms
from .models import LoginForm

class Loginscreen(forms.ModelForm):
    class Meta:
        model = LoginForm
        fields = [
            'userid',
            'password',
            'desc',
            'bill',
            'pincode',

        ]