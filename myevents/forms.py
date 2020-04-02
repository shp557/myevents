from django import forms
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 
from myevents.models import Event
from datetime import datetime, timedelta
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from taggit.forms import *
from myevents.choices import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from taggit.forms import TagWidget

class EventForm(forms.ModelForm):

	#basics
    title = forms.CharField(max_length=128, label="Event title")
    description = forms.CharField(widget=forms.Textarea(), required=False)
    join = forms.URLField(max_length=200, required=False, label="Link to join event", initial="http://")
    category = forms.ChoiceField(choices=CAT_CHOICES)

    #datetimepicker
    start = forms.DateTimeField(
    	input_formats=['%m/%d/%Y %I:%M %p'],
        widget=DateTimePicker(
        	options={
        		'useCurrent': True,
        		'collapse': True,
        		'format': 'MM/DD/YYYY hh:mm A',
                'icons': {
                    'time': 'far fa-clock',
                    'date': 'fa fa-calendar',
                },
        	},
        	attrs={
        		'append': 'fa fa-calendar',
        		'icon_toggle': True,
        	}
        ),
        label="Start time",
    )
    end = forms.DateTimeField(
    	input_formats=['%m/%d/%Y %I:%M %p'],
        widget=DateTimePicker(
        	options={
        		'useCurrent': True,
        		'collapse': True,
        		'format': 'MM/DD/YYYY hh:mm A',
                'icons': {
                    'time': 'far fa-clock',
                    'date': 'fa fa-calendar',
                },
        	},
        	attrs={
        		'append': 'fa fa-calendar',
        		'icon_toggle': True,
        	}
        ),
        label="End time",
    )

    tags = TagField(
        widget=TagWidget(
            attrs={
                'data-role': 'tagsinput',
            },
        ),
        label="Keywords",
    )

    class Meta:
        model = Event
        exclude = ('user',)

    def clean(self):
        cleaned_data = super().clean()

        start = cleaned_data.get('start')
        end = cleaned_data.get('end')

        if start and end and end <= start:
            raise forms.ValidationError(
                "Oops. Your event's end must be after start."
            )
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['description'].widget.attrs['rows'] = 4
        self.fields['description'].widget.attrs['columns'] = 15

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
    	model = User
    	fields = ('username', 'email', 'password',)
