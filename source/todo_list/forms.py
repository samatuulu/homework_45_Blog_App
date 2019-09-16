from django import forms
from django.forms import widgets
from todo_list.models import STATUS_CHOICES


class DateInput(forms.DateInput):
    input_type = 'date'


class JobForm(forms.Form):
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial='new', required=True, label='Job Status')
    description = forms.CharField(required=True, widget=widgets.Textarea, label='Description')
    description_more = forms.CharField(widget=widgets.Textarea, label='Description more')
    date_of_completion = forms.DateField(required=False, widget=DateInput)

