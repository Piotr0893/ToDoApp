from django import forms
from django.forms import ModelForm
from .models import Task
from django.forms.widgets import DateInput


class TaskForm(ModelForm):
    status_choices = [(True, 'Completed'), (False, 'Not Completed')]

    Task_Name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Task Name"}))
    Due_Date = forms.DateField(label='', widget=forms.DateInput(attrs={'placeholder': 'Due Date', 'type': 'text', 'onfocus': "(this.type='date')"}))
    Description = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Description"}))
    
    Status = forms.ChoiceField(label='', widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), choices=status_choices)
   
    class Meta:
        model = Task
        fields = ('Task_Name', 'Due_Date', 'Description', 'Status')
