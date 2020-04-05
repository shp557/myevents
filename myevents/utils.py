from myevents.models import Event
from datetime import datetime, timedelta, timezone
from dateutil import tz
from myevents.choices import *

def querySetter(querySet):
	#adjusted to only today and beyond dates!
	myEvents = []
	for event in querySet:

		dt = datetime.utcnow()
		dt_aware = dt.replace(tzinfo=timezone.utc)

		if (dt_aware <= event.end):

			#stylize
			day = extract_date(event.start)
			duration = delta(event.start, event.end)
			time = extract_time(event.start)

			#add custom values
			event.day = day
			event.time = time
			event.duration = duration 

			myEvents.append(event)

	return myEvents

def getToday(querySet):
	todayEvents = []
	for event in querySet:

		#only today's events
		if (datetime.today().date() == event.start.date()) or (datetime.today().date() == event.end.date()):

			#stylize
			day = extract_date(event.start)
			duration = delta(event.start, event.end)
			time = extract_time(event.start)

			#add custom values
			event.day = day
			event.time = time
			event.duration = duration 

			todayEvents.append(event)

	return todayEvents

def get_all_categories():
	return CAT_CHOICES

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

def extract_date(datetime_var):
	datetime_var = utc_to_local(datetime_var)
	if datetime.now().strftime("%Y") ==  datetime_var.strftime("%Y"):
		if datetime.today().date() == datetime_var.date():
			return "Today"
		else:
			return datetime_var.strftime("%a, %b %d")
	return datetime_var.strftime("%b %d %Y")

def extract_time(datetime_var):
	datetime_var = utc_to_local(datetime_var)
	return datetime_var.strftime("%-I:%M %p")

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
