from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
	meetingTitle=models.CharField(max_length=255)
	meetingDate=models.DateField()
	meetingTime=models.TimeField()
	meetingLocation=models.CharField(max_length=255)
	meetingAgenda=models.CharField(max_length=255)
	
	def __str__(self):
		return self.meetingTitle

	class Meta:
		db_table='meeting'

class MeetingMinutes(models.Model):
	meetingId=models.IntegerField(primary_key=True)
	meetingTime=models.TimeField()
	meetingLocation=models.CharField(max_length=255)
	meetingAgenda=models.CharField(max_length=255)

	class Meta:
		db_table='meetingminutes'

class Resource(models.Model):
	resourceName=models.CharField(max_length=255)
	resourceType=models.TextField()
	resourceURL=models.URLField()
	resourceDateEntered=models.DateField()
	userId=models.CharField(max_length=255)
	resourceDescription=models.CharField(max_length=255)

	class Meta:
		db_table="resource"

class Event(models.Model):
	eventTitle=models.CharField(max_length=255)
	eventLocation=models.CharField(max_length=255)
	eventDate=models.DateField()
	eventTime=models.TimeField()
	eventDescription=models.CharField(max_length=255)
	userId=models.CharField(max_length=255)

	class Meta:
		db_table='event'

