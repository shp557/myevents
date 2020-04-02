from django.shortcuts import render
from myevents.models import Event
from myevents.forms import EventForm, UserForm
from taggit.models import Tag
from django.shortcuts import redirect
from django.template.defaultfilters import slugify 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.template.loader import render_to_string
from myevents.utils import *
from django.core import serializers
import logging
import json

logger = logging.getLogger(__name__)

def index(request):
	events = Event.objects.all().order_by('start')
	events_mod = querySetter(events)
	events_tod = getToday(events)
	events_tod
	context_dict = {
		'events': events_mod,
		'today': events_tod,
	}
	return render(request, 'myevents/index.html', context=context_dict)

def table_view(request):
	events = Event.objects.all().order_by('start')
	events_mod = querySetter(events)
	events_tod = getToday(events)
	events_tod
	context_dict = {
		'events': events_mod,
		'today': events_tod,
	}
	return render(request, 'myevents/table_view.html', context=context_dict)

def about(request):
	return render(request, 'myevents/about.html', context = {'boldmessage': 'This was put together by sachinpatel.'})

@login_required
def add_event(request):
	
	form = EventForm()

	if request.method == 'POST':
		form = EventForm(request.POST)

		if form.is_valid():

			event = form.save(commit=False)
			event.user = request.user
			event.save()
			form.save_m2m()

			return redirect(reverse('myevents:index'))

		else:
			print(form.errors)

	context_dict = {'form': form}

	return render(request, 'myevents/add_event.html', context=context_dict)

@login_required
def edit_event(request, event_id):

	myevent = Event.objects.get(id=event_id)

	form = EventForm(instance=myevent)

	if request.method == 'POST':
		form = EventForm(request.POST, instance=myevent)

		if form.is_valid():

			event = form.save(commit=False)
			event.user = request.user
			event.save()
			form.save_m2m()

			return redirect(reverse('myevents:index'))

		else:
			print(form.errors)

	context_dict = {'form': form}

	return render(request, 'myevents/edit_event.html', context=context_dict)

def show_event(request, event_id):

	myEvent = Event.objects.get(id=event_id)
	context_dict = {
		'event': myEvent, 
	}
	logger.error(myEvent)
	if myEvent:
		return render(request, 'myevents/event.html', context=context_dict)
	return HttpResponse("Hm, doesn't seem to be a valid event..")

class SubsetView(View):

	def get(self, request):
		category_id = request.GET['category_id']
		events = Event.objects.all().order_by('start')
		if category_id != 'all':
			events = Event.objects.filter(category=category_id).order_by('start')
			
		myevents = querySetter(events)

		serialized_events = [ob.as_json() for ob in myevents]
		return JsonResponse(serialized_events, safe=False)

@login_required
def profile(request):
	user = request.user
	context_dict = {
		'user': user,
		'events': Event.objects.filter(user=user),
	}
	return render(request, 'myevents/profile.html', context=context_dict)

@login_required
def delete(request, event_id):
	event = Event.objects.get(id=event_id)
	return redirect(reverse('profile'))

