from django import template
from myevents.models import Event
from datetime import datetime, timedelta
from myevents.choices import *
from dateutil.parser import *

register = template.Library()

@register.simple_tag
def get_event_list(current_category):
	if current_category is None:
		return Event.objects.all
	return Event.objects.filter(category=current_category)

@register.simple_tag
def get_all_categories():
	return CAT_CHOICES

@register.simple_tag
def delta(start_time, end_time):
	seconds_diff = (end_time - start_time).total_seconds()
	hrs = round(seconds_diff/3600)
	mins = round(seconds_diff/60)
	sec = round(seconds_diff)
	if hrs < 1:
		if mins < 1:
			return (str(sec) + " s")
		else:
			return (str(mins) + " min")
	return (str(hrs) + " hr")

@register.simple_tag
def extract_date(datetime_var):
	if datetime.now().strftime("%Y") ==  datetime_var.strftime("%Y"):
		return datetime_var.strftime("%b %d")
	return datetime_var.strftime("%b %d %Y")