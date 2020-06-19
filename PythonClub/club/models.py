from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
	meetingTitle=models.CharField(max_length=255)
	meetingDate=models.DateField()
	meetingTime=models.TimeField()
	meetingLocation=
	meetingAgenda=models.CharField(max_length=255)

class MeetingMinutes(models.Model):
	meetingId=
	meetingTime=models.TimeField()
	meetingLocation=
	meetingAgenda=models.CharField(max_length=255)

class Resource(models.Model):
	resourceName=
	resourceType=
	resourceURL=
	resourceDateEntered=models.DateField()
	userId=models.CharField(max_length=255)
	resourceDescription=models.CharField(max_length=255)

class Event(models.Model):
	eventTitle=models.CharField(max_length=255)
	eventLocation=
	eventDate=models.DateField()
	eventTime=models.TimeField()
	eventDescription=models.CharField(max_length=255)
	userId=models.CharField(max_length=255)

