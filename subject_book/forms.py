from django import forms
from django.core.exceptions import ValidationError
from subject_book.models import Subject


class SubjectForm(forms.Form):
    name = forms.CharField(label='name', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))


class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ModelBasedSubjectForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Subject
        fields = ['name',"id"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
