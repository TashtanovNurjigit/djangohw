from django import forms
from . import models


class ShowForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'

