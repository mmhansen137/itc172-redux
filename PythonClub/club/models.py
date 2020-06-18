from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
	meetingTitle
	meetingDate
	meetingTime
	meetingLocation
	meetingAgenda

class MeetingMinutes
	meetingId
	meetingTime
	meetingLocation
	meetingAgenda

class Resource
	resourceName
	resourceType
	resourceURL
	resourceDateEntered
	userId
	resourceDescription

class Event
	eventTitle
	eventLocation
	eventDate
	eventTime
	eventDescription
	userId	
