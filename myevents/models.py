from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify 
from django.utils import timezone
from datetime import datetime, timedelta
from myevents.choices import *

class Event(models.Model):

	#basics
	title = models.CharField(max_length=128)
	description = models.TextField()
	join = models.URLField(max_length=200) 
	tags = TaggableManager()
	category = models.CharField(max_length=128, choices=CAT_CHOICES, default='other')

	#start, end, and duration
	start = models.DateTimeField()
	end = models.DateTimeField()

	#assign user origin
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def as_json(self):
		return dict(
            id=self.id, 
            title=self.title,
            day=self.day, 
            time=self.time,
            duration=self.duration,
            join=self.join,
            description=self.description,
            )






