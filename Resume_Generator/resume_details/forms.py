from django import forms
from .models import Resume_Detail


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume_Detail
        fields = '__all__'
