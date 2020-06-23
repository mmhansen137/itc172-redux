from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
	meetingTitle=models.CharField(max_length=255)
	meetingDate=models.DateField()
	meetingTime=models.TimeField()
	meetingLocation=models.CharField(max_length=255)
	meetingAgenda=models.TextField()
	
	def __str__(self):
		return self.meetingTitle

	class Meta:
		db_table='meeting'
		verbose_name_plural="meetings"

class MeetingMinutes(models.Model):
	meetingTitle=models.ForeignKey(Meeting, on_delete=models.CASCADE)
	mtngAttendance=models.ManyToManyField(User)
	mtngMinutes=models.TextField()

	def __str__(self):
		return self.mtngMinutes

	class Meta:
		db_table='minutes'
		verbose_name_plural="meetingminutes"

class Resource(models.Model):
	resourceName=models.CharField(max_length=255)
	resourceType=models.CharField(max_length=255)
	resourceURL=models.URLField()
	resourceDateEntered=models.DateField()
	userId=models.ForeignKey(User, on_delete=models.CASCADE)
	resourceDescription=models.TextField()

	def __str__(self):
		return self.resourceName

	class Meta:
		db_table='resource'
		verbose_name_plural="resources"

class Event(models.Model):
	eventTitle=models.CharField(max_length=255)
	eventLocation=models.CharField(max_length=255)
	eventDate=models.DateField()
	eventTime=models.TimeField()
	eventDescription=models.TextField()
	userId=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.eventTitle

	class Meta:
		db_table='event'
		verbose_name_plural="events"

