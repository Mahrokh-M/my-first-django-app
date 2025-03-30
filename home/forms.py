from django import forms
from .models import Person


class CreatePerson(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField()


class UpdatePerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
