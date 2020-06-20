from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.

def index (request):
    return render(request, 'club/index.html')

def getmeetings(request):
	meeting_list=Meeting.objects.all()
	return render(request, 'club/meetings.html' ,{'meeting_list' : meeting_list})

def getresources(request):
	resource_list=Resource.objects.all()
	return render(request, 'club/resources.html' ,{'resource_list' : resource_list})

